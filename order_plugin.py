#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小氢云商城下单插件 - AstrBot 版本
用户通过对话完成下单流程
"""

import json
import aiohttp
from astrbot.api import AstrBotConfig, logger
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register

API_BASE = "http://dilmurat.icu/api"


@register(
    "astrbot_plugin_xiaoqingyun",
    "langke06",
    "小氢云商城下单插件，支持学习通/U校园/雨课堂等课程代刷服务",
    "1.0.0",
)
class XiaoQingYunPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config
        # 存储用户会话状态
        self.user_sessions = {}
        logger.info("小氢云商城插件加载完成")

    async def _api_request(self, method: str, endpoint: str, **kwargs):
        """发送API请求"""
        url = f"{API_BASE}{endpoint}"
        async with aiohttp.ClientSession() as session:
            if method == "GET":
                async with session.get(url, **kwargs, timeout=30) as resp:
                    return await resp.json()
            else:
                async with session.post(url, **kwargs, timeout=30) as resp:
                    return await resp.json()

    @filter.command("下单")
    async def start_order(self, event: AstrMessageEvent):
        '''开始下单流程 - 用法：/下单'''
        user_id = event.get_sender_id()
        
        self.user_sessions[user_id] = {"step": "search_goods"}
        
        reply = """🛒 小氢云商城下单助手

请发送商品关键词，例如：
• 学习通
• U校园  
• 雨课堂

或发送商品ID直接下单：
• 1 - 学习通-全包
• 2 - 学习通-单独
• 5 - U校园-整本
• 10 - U校园AI版-单元

💡 输入 "取消" 可随时退出下单流程"""
        
        yield event.plain_result(reply)

    @filter.command("取消")
    async def cancel_order(self, event: AstrMessageEvent):
        '''取消当前下单流程'''
        user_id = event.get_sender_id()
        if user_id in self.user_sessions:
            del self.user_sessions[user_id]
            yield event.plain_result("✅ 已取消下单流程")
        else:
            yield event.plain_result("❌ 当前没有进行中的下单")

    @filter.event_message_type(filter.EventMessageType.ALL)
    async def handle_conversation(self, event: AstrMessageEvent):
        '''处理下单对话流程'''
        user_id = event.get_sender_id()
        message = event.message_str.strip()
        
        # 检查是否有进行中的会话
        if user_id not in self.user_sessions:
            return
        
        session = self.user_sessions[user_id]
        step = session.get("step")
        
        # 处理取消
        if message == "取消":
            del self.user_sessions[user_id]
            yield event.plain_result("✅ 已取消下单流程")
            return
        
        try:
            if step == "search_goods":
                await self._handle_goods_search(event, session, message)
            elif step == "select_goods":
                await self._handle_goods_select(event, session, message)
            elif step == "fill_inputs":
                await self._handle_fill_inputs(event, session, message)
            elif step == "select_course":
                await self._handle_course_select(event, session, message)
            elif step == "confirm_order":
                await self._handle_confirm_order(event, session, message)
        except Exception as e:
            logger.error(f"下单流程错误: {e}")
            yield event.plain_result(f"❌ 处理出错: {str(e)}\n请发送「取消」后重新开始")

    async def _handle_goods_search(self, event, session, message):
        """处理商品搜索"""
        # 检查是否是数字（直接输入商品ID）
        if message.isdigit():
            goods_id = int(message)
            await self._load_goods_detail(event, session, goods_id)
            return
        
        # 搜索商品
        result = await self._api_request("GET", "/goods/search", params={"keyword": message})
        
        if result.get("code") != 200:
            yield event.plain_result("❌ 搜索失败，请重试或输入「取消」退出")
            return
        
        goods_list = result.get("data", [])
        if not goods_list:
            yield event.plain_result("❌ 未找到相关商品，请尝试其他关键词")
            return
        
        session["goods_list"] = goods_list
        session["step"] = "select_goods"
        
        reply = "📦 找到以下商品，请回复编号选择：\n\n"
        for i, goods in enumerate(goods_list, 1):
            price = goods.get("price", "N/A")
            reply += f"{i}. {goods['name']} - ¥{price}\n"
        reply += "\n💡 回复数字选择商品，或回复「取消」退出"
        
        yield event.plain_result(reply)

    async def _handle_goods_select(self, event, session, message):
        """处理商品选择"""
        if not message.isdigit():
            yield event.plain_result("❌ 请输入商品编号（数字）")
            return
        
        choice = int(message) - 1
        goods_list = session.get("goods_list", [])
        
        if choice < 0 or choice >= len(goods_list):
            yield event.plain_result(f"❌ 无效选择，请输入 1-{len(goods_list)} 之间的数字")
            return
        
        selected_goods = goods_list[choice]
        await self._load_goods_detail(event, session, selected_goods["id"])

    async def _load_goods_detail(self, event, session, goods_id):
        """加载商品详情"""
        result = await self._api_request("GET", "/goods/detail", params={"id": goods_id})
        
        if result.get("code") != 200:
            yield event.plain_result("❌ 获取商品详情失败")
            return
        
        goods_detail = result.get("data", {})
        session["goods_id"] = goods_id
        session["goods_detail"] = goods_detail
        session["inputs"] = {}
        session["input_fields"] = []
        
        # 解析输入字段
        inputs_config = goods_detail.get("input", [])
        input_fields = []
        
        for idx, field in enumerate(inputs_config):
            field_type = field.get("types")
            
            if field_type == 9:  # SKU选择
                input_fields.append({
                    "index": idx,
                    "type": "sku",
                    "title": field.get("title", "规格"),
                    "options": field.get("attributes", [])
                })
            elif field_type == 1:  # 文本输入
                input_fields.append({
                    "index": idx,
                    "type": "text",
                    "title": field.get("title", f"字段{idx}")
                })
        
        session["input_fields"] = input_fields
        session["current_input_idx"] = 0
        session["step"] = "fill_inputs"
        
        # 开始填写第一个字段
        await self._ask_next_input(event, session)

    async def _ask_next_input(self, event, session):
        """询问下一个输入字段"""
        input_fields = session["input_fields"]
        current_idx = session["current_input_idx"]
        
        if current_idx >= len(input_fields):
            # 所有字段填写完成，搜索课程
            await self._search_courses(event, session)
            return
        
        field = input_fields[current_idx]
        
        if field["type"] == "sku":
            reply = f"📋 请选择{field['title']}：\n\n"
            for opt in field["options"]:
                reply += f"• {opt.get('value')} (¥{opt.get('price', 'N/A')})\n"
            reply += f"\n请回复规格名称（如：{field['options'][0].get('value', '选项')}）"
        else:
            reply = f"📝 请输入{field['title']}："
        
        yield event.plain_result(reply)

    async def _handle_fill_inputs(self, event, session, message):
        """处理字段填写"""
        input_fields = session["input_fields"]
        current_idx = session["current_input_idx"]
        field = input_fields[current_idx]
        
        # 保存输入值
        session["inputs"][str(field["index"])] = message
        session["current_input_idx"] += 1
        
        # 询问下一个字段
        await self._ask_next_input(event, session)

    async def _search_courses(self, event, session):
        """搜索课程"""
        yield event.plain_result("🔍 正在查询课程列表，请稍候...")
        
        goods_id = session["goods_id"]
        inputs = session["inputs"]
        
        result = await self._api_request(
            "GET", 
            "/goods/courses",
            params={
                "goods_id": goods_id,
                "inputs": json.dumps(inputs)
            }
        )
        
        if result.get("code") != 200:
            yield event.plain_result("❌ 查询课程失败，请检查账号密码是否正确")
            session["step"] = "fill_inputs"
            session["current_input_idx"] = 0
            session["inputs"] = {}
            await self._ask_next_input(event, session)
            return
        
        courses = result.get("data", [])
        if not courses:
            yield event.plain_result("❌ 未找到课程，请检查账号密码")
            session["step"] = "fill_inputs"
            session["current_input_idx"] = 0
            session["inputs"] = {}
            await self._ask_next_input(event, session)
            return
        
        session["courses"] = courses
        session["step"] = "select_course"
        
        reply = "📚 找到以下课程，请回复编号选择：\n\n"
        for i, course in enumerate(courses, 1):
            reply += f"{i}. {course.get('name', '未知课程')}\n"
        reply += "\n💡 回复数字选择课程"
        
        yield event.plain_result(reply)

    async def _handle_course_select(self, event, session, message):
        """处理课程选择"""
        if not message.isdigit():
            yield event.plain_result("❌ 请输入课程编号（数字）")
            return
        
        choice = int(message) - 1
        courses = session.get("courses", [])
        
        if choice < 0 or choice >= len(courses):
            yield event.plain_result(f"❌ 无效选择，请输入 1-{len(courses)} 之间的数字")
            return
        
        selected_course = courses[choice]
        session["course_id"] = selected_course.get("id", "")
        session["course_name"] = selected_course.get("name", "")
        session["step"] = "confirm_order"
        
        # 显示订单确认
        goods_detail = session["goods_detail"]
        reply = f"""📋 订单确认

商品：{goods_detail.get('name', '未知')}
课程：{session['course_name']}

💳 请选择支付方式：
1. 微信支付
2. 支付宝
3. 余额支付

请回复数字（1/2/3）"""
        
        yield event.plain_result(reply)

    async def _handle_confirm_order(self, event, session, message):
        """处理订单确认和创建"""
        pay_map = {"1": "wxpay", "2": "alipay", "3": "type_money"}
        
        if message not in pay_map:
            yield event.plain_result("❌ 无效选择，请回复 1、2 或 3")
            return
        
        pay_type = pay_map[message]
        
        yield event.plain_result("📝 正在创建订单，请稍候...")
        
        # 创建订单
        result = await self._api_request(
            "POST",
            "/order/create",
            data={
                "goods_id": session["goods_id"],
                "pay": pay_type,
                "num": 1,
                "inputs": json.dumps(session["inputs"]),
                "course_id": session["course_id"],
                "course_name": session["course_name"]
            }
        )
        
        if result.get("code") == 201:
            # 下单成功
            order_no = result.get("out_trade_no")
            pay_url = result.get("url")
            
            reply = f"""✅ 订单创建成功！

📦 订单号：{order_no}
📚 课程：{session['course_name']}

💳 支付链接：
{pay_url}

请点击链接完成支付
支付完成后服务将自动开始"""
            
            yield event.plain_result(reply)
        else:
            yield event.plain_result(f"❌ 下单失败：{result.get('msg', '未知错误')}")
        
        # 清理会话
        user_id = event.get_sender_id()
        if user_id in self.user_sessions:
            del self.user_sessions[user_id]

    async def terminate(self):
        '''插件卸载时调用'''
        self.user_sessions.clear()
        logger.info("小氢云商城插件已卸载")

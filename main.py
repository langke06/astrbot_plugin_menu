import aiohttp
import json
from astrbot.api import AstrBotConfig, logger
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register

API_BASE = "http://dilmurat.icu/api"
QUERY_URL = "http://nbwk.online/api/index.php?act=cd"


@register(
    "astrbot_plugin_menu",
    "langke06",
    "菜单插件，支持下单和查进度功能",
    "1.1.0",
)
class MenuPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config
        self.user_sessions = {}
        logger.info("菜单插件加载完成")

    # ==================== 菜单功能 ====================
    @filter.command("菜单")
    async def show_menu(self, event: AstrMessageEvent):
        '''显示功能菜单'''
        user_name = event.get_sender_name()
        
        menu_text = f"""🤖 你好，{user_name}！我是AstrBot助手

📋 功能菜单：
━━━━━━━━━━━━━━━━
🔹 /下单         - 开始下单（学习通/U校园/雨课堂）
🔹 /查进度 <手机号> - 查询订单进度
🔹 /帮助         - 查看详细帮助
━━━━━━━━━━━━━━━━

💡 提示：直接发送「菜单」或输入「/菜单」都可以查看此菜单
        """
        
        logger.info(f"用户 {user_name} 请求了菜单")
        yield event.plain_result(menu_text)

    @filter.command("help")
    async def show_help(self, event: AstrMessageEvent):
        '''显示帮助信息'''
        help_text = """📖 详细帮助

【下单流程】
1. 发送 /下单 开始
2. 输入商品关键词（如：学习通）
3. 选择商品编号
4. 按提示填写信息（规格、账号、密码等）
5. 选择课程
6. 选择支付方式
7. 获取支付链接完成支付

【查进度】
发送：/查进度 手机号
示例：/查进度 19914282289

【取消下单】
发送：取消

💡 有问题请联系管理员
        """
        yield event.plain_result(help_text)

    # ==================== 查进度功能 ====================
    @filter.command("查进度")
    async def query_progress(self, event: AstrMessageEvent, phone: str = ""):
        '''查询订单进度 - 用法：/查进度 手机号'''
        user_name = event.get_sender_name()
        
        if not phone:
            yield event.plain_result("❌ 请输入手机号\n用法：/查进度 手机号")
            return
        
        if not phone.isdigit() or len(phone) != 11:
            yield event.plain_result("❌ 手机号格式不正确，请输入11位数字手机号")
            return
        
        logger.info(f"用户 {user_name} 查询手机号 {phone} 的进度")
        
        try:
            async with aiohttp.ClientSession() as session:
                data = {"username": phone}
                async with session.post(QUERY_URL, data=data, timeout=30) as resp:
                    if resp.status != 200:
                        yield event.plain_result(f"❌ 查询失败，服务器返回状态码：{resp.status}")
                        return
                    
                    result = await resp.json()
                    
                    if result.get("code") != 1:
                        yield event.plain_result(f"❌ 查询失败：{result.get('msg', '未知错误')}")
                        return
                    
                    orders = result.get("data", [])
                    if not orders:
                        yield event.plain_result(f"📭 手机号 {phone} 暂无订单信息")
                        return
                    
                    reply_text = f"📱 手机号：{phone}\n"
                    reply_text += f"📦 共找到 {len(orders)} 个订单\n"
                    reply_text += "━━━━━━━━━━━━━━━━\n\n"
                    
                    for idx, order in enumerate(orders, 1):
                        ptname = order.get("ptname", "未知平台")
                        school = order.get("school", "")
                        kcname = order.get("kcname", "未知课程")
                        status = order.get("status", "未知")
                        process = order.get("process", "0%")
                        addtime = order.get("addtime", "")
                        remarks = order.get("remarks", "")
                        
                        reply_text += f"【订单 {idx}】\n"
                        reply_text += f"📌 平台：{ptname}\n"
                        if school:
                            reply_text += f"🏫 学校：{school}\n"
                        reply_text += f"📚 课程：{kcname}\n"
                        reply_text += f"📊 进度：{process}\n"
                        reply_text += f"✅ 状态：{status}\n"
                        if addtime:
                            reply_text += f"🕐 下单时间：{addtime}\n"
                        if remarks:
                            try:
                                remarks = remarks.encode('latin1').decode('utf-8')
                            except:
                                pass
                            reply_text += f"📝 备注：{remarks}\n"
                        reply_text += "\n"
                    
                    reply_text += "━━━━━━━━━━━━━━━━"
                    yield event.plain_result(reply_text)
                    
        except Exception as e:
            logger.error(f"查询进度异常：{e}")
            yield event.plain_result("❌ 查询出错，请稍后重试")

    # ==================== 下单功能 ====================
    @filter.command("下单")
    async def start_order(self, event: AstrMessageEvent):
        '''开始下单流程'''
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
        
        if user_id not in self.user_sessions:
            return
        
        # 避免处理命令
        if message.startswith("/"):
            return
        
        session = self.user_sessions[user_id]
        step = session.get("step")
        
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

    async def _handle_goods_search(self, event, session, message):
        """处理商品搜索"""
        if message.isdigit():
            goods_id = int(message)
            await self._load_goods_detail(event, session, goods_id)
            return
        
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
        reply += "\n💡 回复数字选择商品"
        
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
        
        inputs_config = goods_detail.get("input", [])
        input_fields = []
        
        for idx, field in enumerate(inputs_config):
            field_type = field.get("types")
            
            if field_type == 9:
                input_fields.append({
                    "index": idx,
                    "type": "sku",
                    "title": field.get("title", "规格"),
                    "options": field.get("attributes", [])
                })
            elif field_type == 1:
                input_fields.append({
                    "index": idx,
                    "type": "text",
                    "title": field.get("title", f"字段{idx}")
                })
        
        session["input_fields"] = input_fields
        session["current_input_idx"] = 0
        session["step"] = "fill_inputs"
        
        await self._ask_next_input(event, session)

    async def _ask_next_input(self, event, session):
        """询问下一个输入字段"""
        input_fields = session["input_fields"]
        current_idx = session["current_input_idx"]
        
        if current_idx >= len(input_fields):
            await self._search_courses(event, session)
            return
        
        field = input_fields[current_idx]
        
        if field["type"] == "sku":
            reply = f"📋 请选择{field['title']}：\n\n"
            for opt in field["options"]:
                reply += f"• {opt.get('value')} (¥{opt.get('price', 'N/A')})\n"
            reply += f"\n请回复规格名称"
        else:
            reply = f"📝 请输入{field['title']}："
        
        yield event.plain_result(reply)

    async def _handle_fill_inputs(self, event, session, message):
        """处理字段填写"""
        input_fields = session["input_fields"]
        current_idx = session["current_input_idx"]
        field = input_fields[current_idx]
        
        session["inputs"][str(field["index"])] = message
        session["current_input_idx"] += 1
        
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
        
        if result.get("code") != 200 or not result.get("data"):
            yield event.plain_result("❌ 查询课程失败，请检查账号密码是否正确")
            session["step"] = "fill_inputs"
            session["current_input_idx"] = 0
            session["inputs"] = {}
            await self._ask_next_input(event, session)
            return
        
        courses = result.get("data", [])
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
        
        user_id = event.get_sender_id()
        if user_id in self.user_sessions:
            del self.user_sessions[user_id]

    async def terminate(self):
        '''插件卸载时调用'''
        self.user_sessions.clear()
        logger.info("菜单插件已卸载")

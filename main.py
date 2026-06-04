import aiohttp
import json
from astrbot.api import AstrBotConfig, logger
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register

QUERY_URL = "http://nbwk.online/api/index.php?act=cd"


@register(
    "astrbot_plugin_menu",
    "langke06",
    "菜单插件，支持查进度和关键词监控功能",
    "1.3.0",
)
class MenuPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config

        # 关键词监控配置
        self.keywords = getattr(config, "keywords", ["广告", "推广", "兼职", "刷单", "诈骗"])
        self.alert_target = getattr(config, "alert_target", "")
        self.monitor_groups = getattr(config, "monitor_groups", [])

        logger.info(f"菜单插件加载完成，关键词监控: {len(self.keywords)} 个关键词")

    # ==================== 菜单功能 ====================
    @filter.command("菜单")
    async def show_menu(self, event: AstrMessageEvent):
        '''显示功能菜单'''
        user_name = event.get_sender_name()
        
        menu_text = f"""🤖 你好，{user_name}！我是AstrBot助手

📋 功能菜单：
━━━━━━━━━━━━━━━━
🔹 /查进度 <手机号> - 查询订单进度
🔹 /帮助         - 查看详细帮助
━━━━━━━━━━━━━━━━

🔔 关键词监控: 已启用
💡 提示：直接发送「菜单」或输入「/菜单」都可以查看此菜单
        """
        
        logger.info(f"用户 {user_name} 请求了菜单")
        yield event.plain_result(menu_text)

    @filter.command("help")
    async def show_help(self, event: AstrMessageEvent):
        '''显示帮助信息'''
        help_text = """📖 详细帮助

【查进度】
发送：/查进度 手机号
示例：/查进度 19914282289

【关键词监控】
- 自动监控群聊中的敏感词
- 触发关键词后会通知管理员
- 可在配置页面设置关键词和通知目标

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

    # ==================== 关键词监控功能 ====================
    @filter.event_message_type(filter.EventMessageType.ALL)
    async def monitor_keywords(self, event: AstrMessageEvent):
        '''监控群聊关键词'''
        # 检查是否是群聊消息
        message_obj = event.message_obj
        if not message_obj.group_id:
            return

        # 检查是否配置了监控
        if not self.keywords or not self.alert_target:
            return

        # 检查是否在监控群列表中（如果配置了的话）
        if self.monitor_groups and message_obj.group_id not in self.monitor_groups:
            return

        message_text = event.message_str

        # 检查是否包含关键词
        matched_keywords = []
        for keyword in self.keywords:
            if keyword in message_text:
                matched_keywords.append(keyword)

        if matched_keywords:
            # 发送警告
            sender = event.get_sender_name()
            group_id = message_obj.group_id

            alert_msg = f"""⚠️ 关键词警告

触发关键词: {', '.join(matched_keywords)}
发送者: {sender}
群聊: {group_id}
消息内容:
{message_text[:200]}{'...' if len(message_text) > 200 else ''}"""

            try:
                # 获取当前消息的 umo 作为参考
                current_umo = event.unified_msg_origin
                
                # 解析当前UMO获取平台名
                # 格式: platform:message_type:session_id
                platform_name = current_umo.split(":")[0] if ":" in current_umo else "aiocqhttp"
                
                # 构建目标UMO
                if self.alert_target.startswith("group:"):
                    target_id = self.alert_target.replace("group:", "")
                    umo = f"{platform_name}:GroupMessage:{target_id}"
                elif self.alert_target.startswith("qq:"):
                    target_id = self.alert_target.replace("qq:", "")
                    umo = f"{platform_name}:FriendMessage:{target_id}"
                else:
                    # 默认作为用户ID发送（私聊）
                    umo = f"{platform_name}:FriendMessage:{self.alert_target}"
                
                # 使用 context.send_message 发送
                from astrbot.api.event import MessageChain
                message_chain = MessageChain().message(alert_msg)
                await self.context.send_message(umo, message_chain)
            except Exception as e:
                logger.error(f"发送关键词警告失败: {e}")

    async def terminate(self):
        '''插件卸载时调用'''
        logger.info("菜单插件已卸载")

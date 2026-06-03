import aiohttp
import json
from astrbot.api import AstrBotConfig, logger
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register


@register(
    "astrbot_plugin_menu",
    "langke06",
    "一个简单的菜单插件，用户发送'菜单'时显示功能列表，支持查进度功能",
    "1.0.4",
)
class MenuPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config
        # 从配置中读取查询地址
        self.query_url = getattr(config, "query_url", "")
        logger.info(f"菜单插件配置加载完成: query_url={self.query_url}")

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

使用说明：
1. 所有指令都可以通过「/指令名」或「指令名」触发
2. 参数用空格分隔，如：/天气 北京
3. 查进度格式：/查进度 手机号
4. 有问题请联系管理员

更多功能正在开发中，敬请期待！
        """
        yield event.plain_result(help_text)

    @filter.command("查进度")
    async def query_progress(self, event: AstrMessageEvent, phone: str = ""):
        '''查询订单进度 - 用法：/查进度 手机号'''
        user_name = event.get_sender_name()
        
        # 检查配置
        if not self.query_url:
            yield event.plain_result("❌ 查询地址未配置，请在插件配置中设置 query_url")
            return
        
        # 检查手机号
        if not phone:
            yield event.plain_result("❌ 请输入手机号\n用法：/查进度 手机号")
            return
        
        # 验证手机号格式（简单验证）
        if not phone.isdigit() or len(phone) != 11:
            yield event.plain_result("❌ 手机号格式不正确，请输入11位数字手机号")
            return
        
        logger.info(f"用户 {user_name} 查询手机号 {phone} 的进度")
        
        try:
            # 发送请求 - 使用 URL 编码格式 (application/x-www-form-urlencoded)
            async with aiohttp.ClientSession() as session:
                url = "http://nbwk.online/api/index.php?act=cd"
                
                # 使用 URL 编码格式数据
                data = {"username": phone}
                
                logger.info(f"请求URL: {url}, data: {data}")
                async with session.post(url, data=data, timeout=30) as resp:
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
                    
                    # 格式化订单信息
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
                            # 处理备注中的UTF-8编码问题
                            try:
                                remarks = remarks.encode('latin1').decode('utf-8')
                            except:
                                pass
                            reply_text += f"📝 备注：{remarks}\n"
                        reply_text += "\n"
                    
                    reply_text += "━━━━━━━━━━━━━━━━"
                    yield event.plain_result(reply_text)
                    
        except aiohttp.ClientError as e:
            logger.error(f"查询进度网络错误：{e}")
            yield event.plain_result("❌ 网络请求失败，请稍后重试")
        except json.JSONDecodeError as e:
            logger.error(f"查询进度JSON解析错误：{e}")
            yield event.plain_result("❌ 服务器返回数据解析失败")
        except Exception as e:
            logger.error(f"查询进度异常：{e}")
            yield event.plain_result(f"❌ 查询出错：{str(e)}")

    async def terminate(self):
        '''插件卸载时调用'''
        logger.info("菜单插件已卸载")

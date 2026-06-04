"""
Nathan-Auth 授权管理系统 API 客户端
提供域名授权管理、封禁解封、查询等功能
"""

import requests
from typing import Optional, Dict, Any
from urllib.parse import urljoin


# ==================== 配置区域 ====================
# 请在这里修改你的配置信息

# 授权系统域名
BASE_URL = "https://auth.dilmurat.icu/"

# 网站安全密钥
WEBKEY = "6N37zrh4R2HrZ5cnHvsep7FPnBGkzEVF"

# 管理员账号（添加授权时使用）
ADMIN_NAME = "Dilmurat0613"

# 管理员密码
ADMIN_PASSWORD = "2020Kaldi@"

# 默认应用ID
DEFAULT_APPID = "1"

# 默认授权天数（0为永久）
DEFAULT_AUTHDATE = "0"

# 默认服务器IP
DEFAULT_IP = "127.0.0.1"

# ==================== 配置区域结束 ====================


class NathanAuthClient:
    """Nathan-Auth 授权管理系统 API 客户端"""

    def __init__(self, base_url: str = BASE_URL, webkey: str = WEBKEY):
        """
        初始化客户端

        Args:
            base_url: 授权系统域名，默认使用配置中的 BASE_URL
            webkey: 网站安全密钥，默认使用配置中的 WEBKEY
        """
        self.base_url = base_url.rstrip('/')
        self.webkey = webkey
        self.api_prefix = "/api/Index"

    def _make_request(self, endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        发送API请求

        Args:
            endpoint: API端点
            params: 请求参数

        Returns:
            API响应数据
        """
        url = urljoin(self.base_url, f"{self.api_prefix}/{endpoint}")
        params['webkey'] = self.webkey

        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"code": "0", "msg": f"请求失败: {str(e)}"}
        except ValueError as e:
            return {"code": "0", "msg": f"解析响应失败: {str(e)}"}

    def query_auth(self, appid: str, url: str) -> Dict[str, Any]:
        """
        查询授权状态

        Args:
            appid: 应用ID
            url: 目标站域名

        Returns:
            授权查询结果
        """
        params = {
            "appid": appid,
            "url": url
        }
        return self._make_request("query_auth", params)

    def check_auth(self, appid: str, url: str, ip: str, authcode: str) -> Dict[str, Any]:
        """
        检测授权

        Args:
            appid: 应用ID
            url: 目标站域名
            ip: 目标站服务器IP
            authcode: 授权码

        Returns:
            授权检测结果
        """
        params = {
            "appid": appid,
            "url": url,
            "ip": ip,
            "authcode": authcode
        }
        return self._make_request("check_auth", params)

    def admin_add_auth(
        self,
        url: str,
        qq: str,
        appid: str = DEFAULT_APPID,
        ip: str = DEFAULT_IP,
        adminname: str = ADMIN_NAME,
        password: str = ADMIN_PASSWORD,
        authdate: str = DEFAULT_AUTHDATE,
        email: Optional[str] = None,
        phone: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        管理员添加授权

        Args:
            url: 授权的网站域名
            qq: 授权的网站站长QQ
            appid: 应用ID，默认使用配置中的 DEFAULT_APPID
            ip: 授权的服务器IP，默认使用配置中的 DEFAULT_IP
            adminname: 管理员用户名，默认使用配置中的 ADMIN_NAME
            password: 管理员密码，默认使用配置中的 ADMIN_PASSWORD
            authdate: 授权天数（0为永久，1为1天），默认使用配置中的 DEFAULT_AUTHDATE
            email: 授权邮箱（可选，默认自动拼接为 QQ@qq.com）
            phone: 授权手机号（可选）

        Returns:
            添加结果
        """
        # 如果没有提供邮箱，自动拼接 QQ@qq.com
        if email is None and qq:
            email = f"{qq}@qq.com"

        params = {
            "appid": appid,
            "url": url,
            "qq": qq,
            "ip": ip,
            "adminname": adminname,
            "password": password,
            "authdate": authdate
        }
        if email:
            params["email"] = email
        if phone:
            params["phone"] = phone

        return self._make_request("admin_add_auth", params)

    def user_add_auth(
        self,
        appid: str,
        url: str,
        qq: str,
        ip: str,
        key: str,
        email: Optional[str] = None,
        phone: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        用户添加授权

        Args:
            appid: 应用ID
            url: 授权的网站域名
            qq: 授权的网站站长QQ
            ip: 授权的服务器IP
            key: 用户密钥
            email: 授权邮箱（可选，默认自动拼接为 QQ@qq.com）
            phone: 授权手机号（可选）

        Returns:
            添加结果
        """
        # 如果没有提供邮箱，自动拼接 QQ@qq.com
        if email is None and qq:
            email = f"{qq}@qq.com"

        params = {
            "appid": appid,
            "url": url,
            "qq": qq,
            "ip": ip,
            "key": key
        }
        if email:
            params["email"] = email
        if phone:
            params["phone"] = phone

        return self._make_request("user_add_auth", params)

    def freeze_auth(self, appid: str, url: str, reason: str) -> Dict[str, Any]:
        """
        禁封授权

        Args:
            appid: 应用ID
            url: 授权域名
            reason: 禁封原因

        Returns:
            禁封结果
        """
        params = {
            "appid": appid,
            "url": url,
            "reason": reason
        }
        return self._make_request("freeze_auth", params)

    def unseal_auth(self, appid: str, url: str) -> Dict[str, Any]:
        """
        解封授权

        Args:
            appid: 应用ID
            url: 授权域名

        Returns:
            解封结果
        """
        params = {
            "appid": appid,
            "url": url
        }
        return self._make_request("unseal_auth", params)

    def del_auth(self, appid: str, url: str) -> Dict[str, Any]:
        """
        删除授权

        Args:
            appid: 应用ID
            url: 授权域名

        Returns:
            删除结果
        """
        params = {
            "appid": appid,
            "url": url
        }
        return self._make_request("del_auth", params)

    def query_auth_up_info(self, appid: str, url: str) -> Dict[str, Any]:
        """
        查询授权所属用户信息

        Args:
            appid: 应用ID
            url: 授权域名

        Returns:
            用户信息
        """
        params = {
            "appid": appid,
            "url": url
        }
        return self._make_request("QueryAuthUpInfo", params)

    def query_auth_up_status(self, appid: str, url: str) -> Dict[str, Any]:
        """
        检测授权所属用户状态

        Args:
            appid: 应用ID
            url: 授权域名

        Returns:
            用户状态
        """
        params = {
            "appid": appid,
            "url": url
        }
        return self._make_request("QueryAuthUpStatus", params)

    def get_applist(self) -> Dict[str, Any]:
        """
        获取应用列表

        Returns:
            应用列表
        """
        params = {}
        return self._make_request("applist", params)

    def user_add(
        self,
        username: str,
        password: str,
        qq: str,
        apistate: str,
        money: str,
        admin_name: str = ADMIN_NAME,
        admin_password: str = ADMIN_PASSWORD,
        email: Optional[str] = None,
        phone: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        创建用户

        Args:
            username: 用户名
            password: 用户密码
            qq: 用户QQ
            apistate: API状态 1开启 2关闭
            money: 账户余额
            admin_name: 管理员账号，默认使用配置中的 ADMIN_NAME
            admin_password: 管理员密码，默认使用配置中的 ADMIN_PASSWORD
            email: 用户邮箱（可选，默认自动拼接为 QQ@qq.com）
            phone: 用户手机号（可选）

        Returns:
            创建结果
        """
        # 如果没有提供邮箱，自动拼接 QQ@qq.com
        if email is None and qq:
            email = f"{qq}@qq.com"

        params = {
            "username": username,
            "password": password,
            "qq": qq,
            "apistate": apistate,
            "money": money,
            "admin_name": admin_name,
            "admin_password": admin_password
        }
        if email:
            params["email"] = email
        if phone:
            params["phone"] = phone

        return self._make_request("user_add", params)

    def create_card(
        self,
        card_act: str,
        count: str,
        appid: str = DEFAULT_APPID,
        authdate: str = DEFAULT_AUTHDATE,
        money: str = "0",
        prefix: str = ""
    ) -> Dict[str, Any]:
        """
        生成卡密

        Args:
            card_act: 卡密类型 1余额卡密 2授权卡密
            count: 生成数量
            appid: 应用ID，默认使用配置中的 DEFAULT_APPID
            authdate: 授权天数（卡密类型为2时必填，0为永久），默认使用配置中的 DEFAULT_AUTHDATE
            money: 卡密余额（卡密类型为1时必填）
            prefix: 卡密前缀（可选，如 APP 则生成 APP_xxxxx）

        Returns:
            生成结果，成功时返回卡密列表
        """
        params = {
            "CardAct": card_act,
            "count": count,
            "appid": appid,
            "authdate": authdate,
            "money": money
        }
        if prefix:
            params["prefix"] = prefix

        return self._make_request("createCard", params)

    def replace_auth(
        self,
        qq: str,
        url: str,
        new_url: str,
        appid: str = DEFAULT_APPID,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        ip: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        更换授权（更改域名）

        Args:
            qq: 授权QQ
            url: 旧授权域名
            new_url: 新授权域名
            appid: 应用ID，默认使用配置中的 DEFAULT_APPID
            phone: 授权手机号（可选）
            email: 授权邮箱（可选，默认自动拼接为 QQ@qq.com）
            ip: 授权IP（可选）

        Returns:
            更换结果
        """
        # 如果没有提供邮箱，自动拼接 QQ@qq.com
        if email is None and qq:
            email = f"{qq}@qq.com"

        params = {
            "appid": appid,
            "qq": qq,
            "url": url,
            "new_url": new_url
        }
        if phone:
            params["phone"] = phone
        if email:
            params["email"] = email
        if ip:
            params["ip"] = ip

        return self._make_request("replace_auth", params)

    def card_auth(
        self,
        appid: str,
        url: str,
        qq: str,
        key: str,
        ip: str = DEFAULT_IP,
        email: Optional[str] = None,
        phone: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        卡密授权（使用卡密自助授权）

        Args:
            appid: 应用ID
            url: 授权的网站域名
            qq: 授权的网站站长QQ
            key: 授权卡密
            ip: 授权的服务器IP，默认使用配置中的 DEFAULT_IP
            email: 授权邮箱（可选，默认自动拼接为 QQ@qq.com）
            phone: 授权手机号（可选）

        Returns:
            授权结果
        """
        # 如果没有提供邮箱，自动拼接 QQ@qq.com
        if email is None and qq:
            email = f"{qq}@qq.com"

        params = {
            "appid": appid,
            "url": url,
            "qq": qq,
            "ip": ip,
            "key": key
        }
        if email:
            params["email"] = email
        if phone:
            params["phone"] = phone

        return self._make_request("create_auth", params)


# ==================== 便捷函数接口 ====================

def create_client(base_url: str = BASE_URL, webkey: str = WEBKEY) -> NathanAuthClient:
    """创建Nathan-Auth客户端实例"""
    return NathanAuthClient(base_url, webkey)


def query_auth(url: str, appid: str = DEFAULT_APPID) -> Dict[str, Any]:
    """查询授权状态"""
    client = create_client()
    return client.query_auth(appid, url)


def admin_add_auth(
    url: str,
    qq: str,
    appid: str = DEFAULT_APPID,
    ip: str = DEFAULT_IP,
    adminname: str = ADMIN_NAME,
    password: str = ADMIN_PASSWORD,
    authdate: str = DEFAULT_AUTHDATE,
    email: Optional[str] = None,
    phone: Optional[str] = None
) -> Dict[str, Any]:
    """管理员添加授权"""
    client = create_client()
    return client.admin_add_auth(url, qq, appid, ip, adminname, password, authdate, email, phone)


def freeze_auth(url: str, reason: str, appid: str = DEFAULT_APPID) -> Dict[str, Any]:
    """禁封授权"""
    client = create_client()
    return client.freeze_auth(appid, url, reason)


def unseal_auth(url: str, appid: str = DEFAULT_APPID) -> Dict[str, Any]:
    """解封授权"""
    client = create_client()
    return client.unseal_auth(appid, url)


def del_auth(url: str, appid: str = DEFAULT_APPID) -> Dict[str, Any]:
    """删除授权"""
    client = create_client()
    return client.del_auth(appid, url)


def get_applist() -> Dict[str, Any]:
    """获取应用列表"""
    client = create_client()
    return client.get_applist()


def create_card(
    card_act: str,
    count: str,
    appid: str = DEFAULT_APPID,
    authdate: str = DEFAULT_AUTHDATE,
    money: str = "0",
    prefix: str = ""
) -> Dict[str, Any]:
    """生成卡密"""
    client = create_client()
    return client.create_card(card_act, count, appid, authdate, money, prefix)


def replace_auth(
    qq: str,
    url: str,
    new_url: str,
    appid: str = DEFAULT_APPID,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    ip: Optional[str] = None
) -> Dict[str, Any]:
    """更换授权（更改域名）"""
    client = create_client()
    return client.replace_auth(qq, url, new_url, appid, phone, email, ip)


def card_auth(
    appid: str,
    url: str,
    qq: str,
    key: str,
    ip: str = DEFAULT_IP,
    email: Optional[str] = None,
    phone: Optional[str] = None
) -> Dict[str, Any]:
    """卡密授权（使用卡密自助授权）"""
    client = create_client()
    return client.card_auth(appid, url, qq, key, ip, email, phone)


if __name__ == "__main__":
    # 测试示例
    print("Nathan-Auth API 客户端")
    print(f"当前配置: {BASE_URL}")
    print("请修改代码顶部的配置信息后使用")

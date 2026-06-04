---
name: "nathan-auth"
description: "Nathan-Auth授权管理系统技能，提供域名授权管理、封禁解封、查询等功能。当用户需要管理Nathan-Auth授权系统、添加授权、封禁域名、解封域名、查询授权状态或删除授权时调用。"
---

# Nathan-Auth 授权管理系统

## 功能概述

本技能用于管理 Nathan-Auth 域名授权系统，提供以下功能：

1. **添加授权** - 管理员添加域名授权
2. **封禁授权** - 禁封指定域名的授权
3. **解封授权** - 解除域名的封禁状态
4. **查询授权** - 查询域名授权状态
5. **删除授权** - 删除指定域名的授权
6. **获取应用列表** - 获取所有应用信息
7. **创建用户** - 创建新用户并设置余额

## 配置参数

使用本技能前需要配置以下参数：

- `base_url`: 授权系统域名，如 `http://nathan.com`
- `webkey`: 网站安全密钥
- `admin_name`: 管理员用户名（添加授权时需要）
- `admin_password`: 管理员密码（添加授权时需要）

## API 方法说明

### 1. 查询授权状态
```python
from nathan_auth import NathanAuthClient

client = NathanAuthClient(base_url, webkey)
result = client.query_auth(appid="1", url="example.com")
```

### 2. 管理员添加授权
```python
result = client.admin_add_auth(
    appid="1",
    url="example.com",
    qq="123456789",
    ip="127.0.0.1",
    adminname="admin",
    password="123456",
    authdate="0",  # 0为永久
    email="test@example.com",  # 可选
    phone="13800138000"  # 可选
)
```

### 3. 封禁授权
```python
result = client.freeze_auth(
    appid="1",
    url="example.com",
    reason="违规使用"
)
```

### 4. 解封授权
```python
result = client.unseal_auth(
    appid="1",
    url="example.com"
)
```

### 5. 删除授权
```python
result = client.del_auth(
    appid="1",
    url="example.com"
)
```

### 6. 获取应用列表
```python
result = client.get_applist()
```

### 7. 创建用户（带余额）
```python
result = client.user_add(
    username="newuser",
    password="123456",
    qq="123456789",
    apistate="1",  # 1开启 2关闭
    money="100",   # 账户余额
    admin_name="admin",
    admin_password="123456"
)
```

## 响应格式

所有接口返回统一格式：

```json
{
    "code": "1",     // 1为成功，0为失败
    "msg": "操作成功", // 提示信息
    "data": {}       // 可选，返回数据
}
```

## 使用示例

### 场景1：添加域名授权
用户说："给 example.com 添加授权，QQ是123456789"

```python
from nathan_auth import NathanAuthClient

client = NathanAuthClient("http://nathan.com", "Nathan_Auth")
result = client.admin_add_auth(
    appid="1",
    url="example.com",
    qq="123456789",
    ip="127.0.0.1",
    adminname="admin",
    password="123456",
    authdate="0"
)
print(result["msg"])
```

### 场景2：封禁域名
用户说："封禁 example.com，原因是违规使用"

```python
result = client.freeze_auth(
    appid="1",
    url="example.com",
    reason="违规使用"
)
print(result["msg"])
```

### 场景3：查询授权状态
用户说："查询 example.com 的授权状态"

```python
result = client.query_auth(appid="1", url="example.com")
print(result["msg"])
```

### 场景4：解封域名
用户说："解封 example.com"

```python
result = client.unseal_auth(appid="1", url="example.com")
print(result["msg"])
```

### 场景5：删除授权
用户说："删除 example.com 的授权"

```python
result = client.del_auth(appid="1", url="example.com")
print(result["msg"])
```

## 注意事项

1. 所有接口都需要提供正确的 `webkey` 进行认证
2. 管理员操作需要提供管理员账号和密码
3. `authdate` 参数：0表示永久授权，1表示1天，以此类推
4. 封禁操作需要提供封禁原因
5. 删除操作不可恢复，请谨慎操作

# Nathan-Auth AstrBot 插件开发计划

## 任务概述

将 nathan-auth 技能封装为 AstrBot 插件，支持管理员自定义授权配置，使用 `/plan` 命令进行管理。

## 当前状态分析

### 已有资源

1. **nathan\_auth.py** - 完整的 Nathan-Auth API 客户端，包含以下功能：

   * 查询授权状态

   * 管理员添加授权

   * 封禁/解封授权

   * 删除授权

   * 获取应用列表

   * 创建用户

   * 生成卡密

   * 更换授权域名

   * 卡密授权

2. **现有 AstrBot 插件参考** (order\_plugin.py, main.py)：

   * 使用 `@register` 装饰器注册插件

   * 使用 `@filter.command` 定义命令

   * 使用 `AstrBotConfig` 进行配置管理

   * 异步编程模式

## 设计方案

### 插件结构

```
astrbot_plugin_nathan_auth/
├── __init__.py          # 插件入口
├── main.py              # 主插件类
├── nathan_auth_client.py # API客户端（从现有代码提取）
└── config_template.yaml  # 配置模板
```

### 功能规划

#### 1. 配置管理

* 支持通过 AstrBot 配置页面设置：

  * `base_url`: 授权系统域名

  * `webkey`: 网站安全密钥

  * `admin_name`: 管理员用户名

  * `admin_password`: 管理员密码

  * `default_appid`: 默认应用ID

  * `default_authdate`: 默认授权天数

  * `default_ip`: 默认服务器IP

#### 2. 命令设计

| 命令                          | 功能       | 权限  |
| --------------------------- | -------- | --- |
| `/plan`                     | 显示授权管理菜单 | 管理员 |
| `/plan 查询 <域名>`             | 查询域名授权状态 | 管理员 |
| `/plan 添加 <域名> <QQ>`        | 添加域名授权   | 管理员 |
| `/plan 封禁 <域名> <原因>`        | 封禁域名授权   | 管理员 |
| `/plan 解封 <域名>`             | 解封域名授权   | 管理员 |
| `/plan 删除 <域名>`             | 删除域名授权   | 管理员 |
| `/plan 应用列表`                | 获取应用列表   | 管理员 |
| `/plan 生成卡密 <类型> <数量>`      | 生成卡密     | 管理员 |
| `/plan 更换 <旧域名> <新域名> <QQ>` | 更换授权域名   | 管理员 |

#### 3. 权限控制

* 通过配置 `admin_qq` 或 `admin_groups` 限制可使用命令的用户/群组

## 实施步骤

### 步骤 1: 创建插件目录结构

创建 `astrbot_plugin_nathan_auth/` 文件夹

### 步骤 2: 创建 API 客户端模块

将 `nathan_auth.py` 中的 `NathanAuthClient` 类提取到 `nathan_auth_client.py`

* 移除硬编码配置

* 改为通过构造函数传入配置

### 步骤 3: 创建主插件类

在 `main.py` 中实现：

* 插件注册

* 配置加载

* 命令处理

* 权限检查

### 步骤 4: 创建配置文件模板

`config_template.yaml` 包含所有可配置项的说明

### 步骤 5: 创建 `__init__.py`

插件入口文件

## 文件变更清单

### 新建文件

1. `astrbot_plugin_nathan_auth/__init__.py`
2. `astrbot_plugin_nathan_auth/main.py`
3. `astrbot_plugin_nathan_auth/nathan_auth_client.py`
4. `astrbot_plugin_nathan_auth/config_template.yaml`

## 验证步骤

1. 插件加载测试
2. 配置读取测试
3. 各命令功能测试
4. 权限控制测试

## 注意事项

1. 保持与现有 nathan\_auth.py 的 API 兼容性
2. 使用异步 HTTP 请求 (aiohttp)
3. 完善的错误处理和日志记录
4. 中文回复消息


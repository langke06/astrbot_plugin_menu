# 全局公共参数

**全局Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**全局Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**全局Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**全局认证方式**

> 无需认证

# 状态码说明

| 状态码 | 中文描述 |
| --- | ---- |
| 暂无参数 |

# 安装说明【必看】

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-22 12:29:29

> 更新时间: 2024-05-31 10:04:09

##### 【系统环境】

**PHP版本：PHP7.3版本,PHP扩展：fileinfo，Swoole Compiler,Swoole Compiler需根据首页引导安装拓展！，请务必先安装自己需要的拓展，最后再安装 Swoole Compiler 如未出现引导则已安装,MySQL版本：MySQL 5.6 （其他版本自测）,伪静态：Thinkphp,运行目录：/public**

**Query**

# 接口调用须知【必看】

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-22 12:30:36

> 更新时间: 2024-09-18 10:46:55

**接口中的 网站域名 均为 授权域名（主域名/域名授权系统域名）,接口中的 机器人授权官网域名 均为 后台添加的机器人授权官网域名**

#### 调用须知：

**所有接口，均支持 GET 或者 POST 请求，除某些接口中说明了请求类型的**

#### 返回参数说明

**所有接口，返回成功参数均为 code，提示信息参数为 msg，数据为：data,如：{"code": "1","msg": "查询成功"}**

**[object Object]**

**code为1则为成功，0为失败**

**Query**

# 公共

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:28:38

> 更新时间: 2023-05-15 13:28:38

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 【Public】获取友情链接列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2022-03-23 22:20:41

> 更新时间: 2024-05-31 10:12:46

**请求示例
http://nathan.com/api/Index/linklist?webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/linklist

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> //网站域名/api/Index/linklist?apipost_id=184db39

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "id": 1,
    "name": "南逸博客",
    "url": "http://www.nanyinet.com/",
    "time": "2022-03-20 16:01:05",
    "state": "1"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

## 【Public】获取授权站公告

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2022-03-23 21:34:00

> 更新时间: 2024-05-31 10:04:09

**请求示例
http://nathan.com/api/Index/auth_notice?webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/auth_notice

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> //网站域名/api/Index/auth_notice?apipost_id=184d8af

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "id": 1,
    "title": "公告标题",
    "content": "公告内容",
    "username": "发布者",
    "time": "发布时间",
    "state": "1"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

# 域名授权系统

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:28:44

> 更新时间: 2023-08-02 15:15:09

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## V1版

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-01-08 14:38:00

> 更新时间: 2026-01-08 14:41:47

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 【Url】授权查询

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/query_auth?appid=1&url=nathan.com**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/query_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | nathan.com | string | 是 | 目标站域名 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "正版授权"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Url】授权检测

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/check_auth?appid=1&url=test.com&ip=127.0.0.1&authcode=7c71383d3940e080d42dcca468c6cfb9**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/check_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | nathan2.com | string | 是 | 目标站的网站域名 |
| ip | 127.0.0.1 | string | 是 | 目标站的服务器IP |
| authcode | d631e8af94de8eb641e628784eeb835c | string | 是 | 目标站的网站授权码 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"code": "1",
	"msg": "正版授权，授权期限：永久授权",
	"data": {
		"appid": "1",
		"url": "nathan.com",
		"authcode": "123456",
		"authdate": "永久授权",
		"token": "eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6MSwiaWQiOjF9.kEpJQNbsm6qjsJwDV7r7628cmwutCyhA-X3Do8nfCVY"
	}
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "错误信息提示"
}
```

**Query**

### 【Url】代理查询

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/query_agent?appid=1&type=username&value=2322796106**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/query_agent?appid=1&type=username&value=2322796106

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| type | username | string | 是 | 查询类型 四个类型（username，qq ，email，phone） |
| value | 2322796106 | string | 是 | 查询的内容 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"code": "1",
	"msg": "您查询的用户为此应用的 总销商 可放心交易！"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "您查询的用户QQ不是代理，请停止交易！"
}
```

**Query**

### 【Url】卡密授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/create_auth?appid=1&qq=2322796106&url=nathan.com&ip=127.0.0.1&email=2322796106@qq.com&phone=17777777777&key=EnrB-K441-vG4l-tVKq**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/create_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | 2322796106 | string | 是 | 授权的QQ |
| url | nathan.com | string | 是 | 授权的域名 |
| ip | 127.0.0.1 | string | 是 | 目标站的服务器IP |
| email | 2322796106@qq.com | string | 否 | 授权邮箱 |
| phone | 17777777777 | string | 否 | 授权手机号 |
| key | EnrB-K441-vG4l-tVKq | string | 是 | 授权卡密 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"code": "1",
	"msg": "自助授权：nathan.com 成功！"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "该卡密已被使用，无法授权！"
}
```

**Query**

### 【Url】用户添加授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/user_add_auth?appid=1&url=nathan.com&qq=2322796106&ip=127.0.0.1&email=2322796106@qq.com&phone=17777777777&key=OgP5U1NvBnqjVi6y**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/user_add_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | nathan.com | string | 是 | 授权的网站域名 |
| qq | 2322796106 | string | 是 | 授权的网站站长QQ |
| ip | 127.0.0.1 | string | 是 | 授权的服务器IP |
| email | 2322796106@qq.com | string | 否 | 授权邮箱 |
| phone | 17777777777 | string | 否 | 授权手机号 |
| key | OgP5U1NvBnqjVi6y | string | 是 | 用户密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "添加授权：nathan.com 成功！"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "账户不存在！"
}
```

**Query**

### 【Url】管理员添加授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/admin_add_auth?appid=1&url=test.com&qq=2322796106&ip=127.0.0.1&email=2322796106@qq.com&phone=17777777777&authdate=1&adminname=admin&password=123456**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/admin_add_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | test.com1 | string | 是 | 授权的网站域名 |
| qq | 2322796106 | string | 是 | 授权的网站站长QQ |
| ip | 127.0.0.1 | string | 是 | 授权的服务器IP |
| email | 2322796106@qq.com | string | 否 | 授权邮箱 |
| phone | 17777777777 | string | 否 | 授权手机号 |
| authdate | 0 | string | 是 | 授权天数（0为永久，1为1天） |
| adminname | admin | string | 是 | 管理员用户名 |
| password | 123456 | string | 是 | 管理员密码 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "添加授权：nathan.com 成功！"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "管理员账户不存在！"
}
```

**Query**

### 【Url】获取应用列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/applist?webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/applist

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
[
	{
		"id": "应用ID",
		"app_name": "应用名称",
		"app_team": "团队名称",
		"app_url": "官方网站",
		"app_author": "应用作者",
		"app_qq": "作者QQ",
		"app_file": "授权配置文件位置",
		"app_tips": "未授权提示",
		"app_auth_money": "授权单价",
		"app_addtime": "添加时间",
		"app_isauthcode": "是否开启授权码检测（success为开启，error为关闭）",
		"state": "1"
	},
	{
		"id": 2,
		"app_name": "授权系统",
		"app_team": "Nathan",
		"app_url": "Nathan.com",
		"app_author": "Nathan",
		"app_qq": "2322796106",
		"app_file": "/config/auth.php",
		"app_tips": "您未授权此系统",
		"app_auth_money": "10.00",
		"app_addtime": "2022-03-17 19:28:16",
		"app_isauthcode": "success",
		"state": "1"
	}
]
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Url】获取应用信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/appinfo?appid=1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/appinfo

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
		"id": "应用ID",
		"app_name": "应用名称",
		"app_team": "团队名称",
		"app_url": "官方网站",
		"app_author": "应用作者",
		"app_qq": "作者QQ",
		"app_file": "授权配置文件位置",
		"app_tips": "未授权提示",
		"app_auth_money": "授权单价",
		"app_addtime": "添加时间",
		"app_isauthcode": "是否开启授权码检测（success为开启，error为关闭）",
		"state": "1"
	}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Url】获取版本列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/version_list?appid=1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/version_list

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
[
    {
        "id": 1,
        "appid": "应用ID",
        "version": "版本号",
        "content": "更新内容",
        "complete_file": "完整包地址",
        "update_file": "更新包地址",
        "sql_file": "SQL语句",
        "appname": "应用名称",
        "add_time": "创建时间"
    },
    {
		"id": 2,
		"appid": 1,
		"version": "1.0",
		"content": "发布",
		"complete_file": "upload/complete_zip/123",
		"update_file": "upload/update_zip/123",
		"sql_file": "ALTER TABLE `user` ADD COLUMN `uselength` varchar(11) DEFAULT NULL;",
		"appname": "授权系统",
		"add_time": "2022-03-18 00:00:00"
	}
]
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Url】获取系统公告

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/notice?appid=1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/notice

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
[
    {
        "id": 1,
        "title": "公告标题",
        "content": "公告内容",
        "username": "创建者",
        "appid": 1,
        "appname": "我的系统",
        "time": "2022-00-00",
        "state": "1"
    }
]
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Url】获取货源列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/recommend?appid=1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/recommend

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
[
    {
        "id": 1,
        "webname": "网站名称",
        "webqq": "客服QQ",
        "http": "协议头",
        "domain": "网站域名",
        "money": "认证金额",
        "introduction": "网站说明",
        "appid": "所属应用ID",
        "appname": "所属应用名称",
        "addtime": "创建时间",
        "state": "1"
    }
]
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Url】认证站点查询

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/SiteAuth?appid=1&url=pay.nanyinet.com**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/SiteAuth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | pay.nanyinet.com | string | 是 | 目标站域名 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"code": "1",
	"msg": "www.nanyinet.com 为认证站点"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "pay.nanyinet.com 没有进行站点认证"
}
```

**Query**

### 【Url】认证站点列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/SiteAuthList?appid=1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/SiteAuthList

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
[
	{
		"id": 1,
		"appid": "应用ID",
		"appname": "应用名称",
		"name": "站点名称",
		"url": "站点地址",
		"date": "添加时间",
		"state": "1"
	}
]
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "该应用不存在！"
}
```

**Query**

### 【Url】获取授权信息旗下授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/index/qq_auth?appid=1&type=qq&value=2322796106&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/qq_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 否 | 应用ID（不传则为全部应用） |
| type | qq | string | 是 | 查询类型 三个类型（qq ，email，phone） |
| value | 2322796106 | string | 是 | 查询的内容 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": 1,
    "msg": "查询的授权信息为 17777777778 旗下授权成功",
    "data": [
        {
            "id": 2,
            "url": "www.nanyinet.com",
            "qq": "2322796106",
            "addtime": "2023-01-14 20:14:19",
            "username": "admin",
            "appid": 1,
            "appname": "Nathan_Auth授权系统",
            "authcode": "60e047f4b7a87efa4e8cab268946b81e",
            "authdate": "0",
            "reason": null,
            "ip": "127.0.0.1",
            "email": "2322796106@qq.com",
            "phone": "17777777778",
            "state": "1"
        }
    ]
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Url】获取域名授权码

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/UrlAuthCode?appid=1&url=nathan.com&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/UrlAuthCode

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | nathan.com | string | 是 | 授权域名 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "data": {
        "url": "www.nanyinet.com",
        "qq": "2322796106",
        "authcode": "d631e8af94de8eb641e628784eeb835c"
    }
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Url】更改授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:29:51

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/replace_auth?appid=1&webkey=Nathan_Auth&qq=2322796106&url=nathan.com&new_url=nathan2.com&phone=17777777777&email=2322796106@qq.com&ip=127.0.0.1**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/replace_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| qq | 2322796106 | string | 是 | 授权QQ |
| url | nathan.com | string | 是 | 旧授权域名 |
| new_url | nathan2.com | string | 是 | 新授权域名 |
| phone | 17777777777 | string | 否 | 授权手机号 |
| email | 2322796106@qq.com | string | 否 | 授权邮箱 |
| ip | 127.0.0.1 | string | 否 | 授权IP |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "更换授权信息成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Url】获取授权上级信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:53:15

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/QueryAuthUpInfo?appid=1&url=nathan.com&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/QueryAuthUpInfo

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | nathan.com | string | 是 | 授权域名 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "data": {
        "username": "admin",
        "userqq": "2322796106"
    }
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Url】禁封授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-08-02 14:45:28

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/freeze_auth?appid=1&url=nathan.com&reason=无理由封了&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/freeze_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | nathan.com | string | 是 | 授权域名 |
| reason | 无理由封了 | string | 是 | 禁封原因 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "禁封授权：nathan.com 成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Url】解封授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-08-02 14:53:35

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/unseal_auth?appid=1&url=nathan.com&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/unseal_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | nathan.com | string | 是 | 授权域名 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "解封授权：nathan.com 成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Url】删除授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-08-02 14:56:33

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/del_auth?appid=1&url=nathan.com&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/del_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | nathan.com | string | 是 | 授权域名 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "删除授权：nathan.com 成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Url】获取版本信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-20 19:44:31

> 更新时间: 2026-03-19 10:26:33

**请求示例
http://nathan.com/api/Index/version?appid=1&url=test.com&authcode=7c71383d3940e080d42dcca468c6cfb9&version=1.1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/version

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | test.com | string | 是 | 授权域名 |
| authcode | 7c71383d3940e080d42dcca468c6cfb9 | string | 是 | 目标站的授权码 |
| version | 1.1 | string | 是 | 应用版本号（不填则默认获取最新版） |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "id": 1,
    "appid": 1,
    "appname": "我的系统",
    "version": "1.0",
    "update_zip": "目标站的程序更新包下载地址",
    "update_sql": "SQL语句",
    "force_update": 1,
    "date": "发布时间"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Url】盗版入库

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-20 19:47:49

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/pirated?url=test.com&dbname=nathan_dbname&username=nathan_username&password=nathan_password&appid=1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/pirated

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| url | test.com | string | 是 | 域名 |
| dbname | nathan_dbname | string | 是 | 数据库名 |
| username | nathan_username | string | 是 | 数据库用户名 |
| password | nathan_password | string | 是 | 数据库密码 |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "该域名已成功入库！"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Url】创建用户

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-21 23:08:00

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/user_add?username=admin&password=123456&qq=2322796106&email=2322796106@qq.com&phone=17777777777&apistate=1&money=1&admin_name=admin&admin_password=123456**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/user_add

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| username | admin | string | 是 | 用户名 |
| password | 123456 | string | 是 | 用户密码 |
| qq | 2322796106 | string | 是 | 用户QQ |
| email | 2322796106@qq.com | string | 否 | 用户邮箱 |
| phone | 17777777777 | string | 否 | 用户手机号 |
| apistate | 1 | string | 是 | API状态 1开启 2关闭 |
| money | 1 | string | 是 | 账户余额 |
| admin_name | admin | string | 是 | 管理员账号 |
| admin_password | 123456 | string | 是 | 管理员密码 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "添加用户：admin 成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "该账号已存在，请更换账号！"
}
```

**Query**

### 【Url】检测授权所属用户状态

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-28 21:03:31

> 更新时间: 2026-01-08 14:41:01

**请求示例
http://nathan.com/api/Index/QueryAuthUpStatus?appid=1&url=nathan.com&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/Index/QueryAuthUpStatus

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| url | nathan.com | string | 是 | 授权域名 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "data": {
        "Url": "nathan.com",
        "UserName": "administrator",
        "statusCode": "1",
        "statusMsg": "用户状态正常"
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 获取成功 | string | - |
| data | - | object | - |
| data.Url | nathan.com | string | 授权域名 |
| data.UserName | administrator | string | 所属用户名 |
| data.statusCode | 1 | string | 状态码 1正常 0异常 |
| data.statusMsg | 用户状态正常 | string | 状态描述 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Url】生成卡密

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-03-26 16:39:37

> 更新时间: 2026-01-08 14:41:01

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/createCard?webkey=Nathan_Auth&CardAct=1&count=10&appid=1&authdate=0&money=20&prefix=APP

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| CardAct | 1 | string | 是 | 卡密类型 1余额卡密 2授权卡密 |
| count | 10 | string | 是 | 生成数量 |
| appid | 1 | string | 是 | 应用ID（卡密类型为2必填） |
| authdate | 0 | string | 是 | 授权天数（卡密类型为2必填，0为永久 1为1天） |
| money | 20 | string | 是 | 卡密余额（卡密类型为1必填） |
| prefix | APP | string | 否 | 卡密自定义前缀字段（如：Nathan ,生成的卡密就是Nathan_KEY，此字段可为空） |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "生成10张卡密成功",
    "data": [
        "APP_xYQM-vIWF-uUrU-6vS2",
        "APP_Y84j-iUhW-PjG4-iKfy",
        "APP_ITRT-N9pC-343J-uo0A",
        "APP_TSUZ-Ql2g-F1RZ-uLPe",
        "APP_BxjK-ZePm-kr6D-Rr34",
        "APP_oV1V-E9lB-lyRa-7Nke",
        "APP_6TAj-5kqa-lT2L-SurY",
        "APP_s48E-VcnP-txHy-P6xc",
        "APP_OJiB-na6a-kyYt-25hO",
        "APP_kX4n-6Q0S-o9CL-d8Rk"
    ]
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 生成10张卡密成功 | string | 返回文字描述 |
| data | - | array | 生成的卡密列表 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Url】查询应用自定义参数

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-03-26 18:19:10

> 更新时间: 2026-01-08 14:41:01

**Token为授权检测成功后返回的，详细可见授权检测接口**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/QueryAppParams?token=1&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "data": {
        "key": "Nathan",
        "Auth": "自定义参数"
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 获取成功 | string | - |
| data | - | object | 自定义的参数信息 |
| data.key | Nathan | string | - |
| data.Auth | 自定义参数 | string | - |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Url】验证授权Token是否有效

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-03-28 10:35:46

> 更新时间: 2026-01-08 14:41:01

**Token为授权检测成功后返回的，详细可见授权检测接口**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/verifyAuthToken?token=1

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "Token有效"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | Token有效 | string | 返回文字描述 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "Token无效或已过期"
}
```

**Query**

### 【Url】RSA生成签名

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-18 10:08:43

> 更新时间: 2026-01-08 14:41:01

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/signRSACert

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6MSwiaWQiOjF9.kEpJQNbsm6qjsJwDV7r7628cmwutCyhA-X3Do8nfCVY | string | 是 | Token （授权检测成功后返回的） |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQIN+V0x8nPpAUCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECCntqZEfC4+KBIIEyPzZoJjHrkyr vwR/7zqEI61+2GI2zqDTobsbjGT+4N50a9yMz6w8BwXWIfrNZzU+aT2GQZOcwloU CuY/NE2iXHQIRA637y1gmT+WtzoZplpSFsOmXmNflp9sueIKuLTlu6J6X+RyoQN9 QOTSyOe2iTY0O34Vck+GVZfyFNTrWdeGQmejFlEAfCCFgJ5DYYXSxUV1YUB0tQfF Q/w8H0eOxYp03t+rE/37cwkVf0zKddSWJzi39s0nZov40TV9d2CfUolrSWWgVyB4 Oa19OkKgEA0+cvXd2hiQgGhkCnFw3uYedkaJvMxcfzkYAr/5U62698wnZYL5yTox sbosjxBXjqwft6n49IKZ6ofpKdr8jIcxgZ2wKQ28lrZeKsivGqN8O+8ums0MRHZR 4OPtpffObNegvnF2vwNNrrpi0Xnz9ZoX5nNNqAabgidhV6gnxmr2cPd33vUowL2T q4TBgNBGwasnjEC2V14kpaiHDk7CLxP7BUaOdkKdCmf/9WVNJz+3pQpvb4wx4jh0 koQDA+nUwpQJj+0UvFmZF2fd0sHmyftZ4N6cFDk1ymYFz9sRT0zWiBEDKuK6XCXv xRV88VTf65fLvdKnP94FuCeeEneeJRgtFjlXIehvtqGj2RbamSXyNdWcg1F46sku 8smIV+Pvh6VbCLLMQ8+wjzCzZmOMrAUu0BM11IFneIXWlXH9Oe/BmGAxy1ucWBnM OZpnSgvv2dkJTjCyCyt84j1YA4TttkQaXuhDsZ5Bebxl417u+xN8+JXL/6rd6xVG NHl+soxXphw75o5EcuqL+AYxaN8rRCZl9Wh9an3jcca5WFjI7a5v6UAnDii3O/nS W5CWOzEjptbKwJ+A+9V6OyvfKxDg9aD84BsMs3iMVP6b9RTT7oY54TnTlVMclreh cpZ4bn4t8a30EhSqjoJBDB2izYLajbLV/TraPCpURvS6c1HrjMt6N0wDitnJkV7N y5i22CaL5igFln8SaWORCXPBNUoFBcViWpLt2SLznEEjru0xnFStjgnnZLp3Qi3y QUxQ4oWyoOS/45VW3mUVffEx6GfAaUKG9OSpVNBoSZYPtp+y1XbLSI9PBT3KF0sp ekJ3Mti/b1+rVTgSHDuc0qm1bhyDghO/YtEly4xboHGCjPU+ILh48CNZKkEweyDR 4efsSMYm7jv4v90kEuoeP8zVf8a9FR0JBi5cG0g3s/sngpR7ffMjdaWG3G8DEV3U 3S2vppkCwdjh6ZLk4O1Ihnp+8CIRH2Fy/H/1OWQIMy1DRhn+QxLj86c7S/ILhILh o0KJbzcXoi5Fn9R4k+QYxhRzqJG2kIdRYpOhZeFogeYhu0HNsP8y8FamNXW8qaCD 6Ah8y6VqRlnGQmrqfyRqKMLAdz1sOfOg5goOwKJ4+ctiVu8dK8Cx2KSIevlrkbRt /z14ue0uTLJ3aKB47Ue9c7l9Zsktb+zxhHUBmcec3zFu8G25TFvLN0wo5Ikaeb+z 2q3//7w4XEZmk1QlWyIGvmIl75HYbEsc+JAOsG1P12ZnGO3AFXSh14+gl8wmi25v ultmEP736tHPlE6YnWuZBlDBoA5lx4aSH8STRx5cK+flHwxoRYlOxzWWIT2WyTlm pORKjX/Xx1X52yfNawzkXA== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznTRi08IqmpaxZvXT2x5 gBBqpXuj+/8ryc85w3zAO5ZG63QlAIs5+yE+jYCjJjABhQiTCWl0QWeKZxWCFUAy weXo1XV7klleohVo2hmgWFLZ+IXKEAZdS5dfHfBFYghlgZuxpP3TeUFFIRUd9GD1 d+A30SPfJ1+TbT3STFabgo/wM5pkrvmkhNgNEv1UfHksZVobT34jIJ71FnC2rjr+ tPdMa2IBTM7zZj6ktx9Qha3ZMm7jA7/1gnq0DOCVhtL80TElAc0CboLdHpWblF7H uolyA8N8ND2OFEmghUZI1imdm+oHLqVhcLuDPDcLPxSUypC3bDUnW+HiIR4oJUHO OQIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| sign_data | Nathan | string | 是 | 需签名的内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"签名成功","signature":"SFtu7T\/caVivKIydlFwyahtgldrA0dyTQI+CR6HQS37wOT+cykA3AxndSrpwZcC3dqweU9uR4\/hYmyt0VLgIkPc\/Gg+QLYo19w2qVbpZVSfRn9XmXasChojkK0kpjAx+BdMWNlXO\/lZsEt3S+tHwUw7sU4ZwAikrIwuR7+qsKz2MYVCoNfJUQTKSODtTOp1P6BMnopBDQO2+3P+8X\/z2yTcIXeCw+SA23QLWM89IMXZy0W+F30JUiWxJLkORq\/1zz6bJfl7nZHxHHLA0ksWDngNFQslArvBY2SQihFN4zfBumi+BN48J+2YtfcyJUWZLjpIE\/WQO8HmKSwKySmlOiQ=="}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 签名成功 | string | 返回文字描述 |
| signature | SFtu7T/caVivKIydlFwyahtgldrA0dyTQI+CR6HQS37wOT+cykA3AxndSrpwZcC3dqweU9uR4/hYmyt0VLgIkPc/Gg+QLYo19w2qVbpZVSfRn9XmXasChojkK0kpjAx+BdMWNlXO/lZsEt3S+tHwUw7sU4ZwAikrIwuR7+qsKz2MYVCoNfJUQTKSODtTOp1P6BMnopBDQO2+3P+8X/z2yTcIXeCw+SA23QLWM89IMXZy0W+F30JUiWxJLkORq/1zz6bJfl7nZHxHHLA0ksWDngNFQslArvBY2SQihFN4zfBumi+BN48J+2YtfcyJUWZLjpIE/WQO8HmKSwKySmlOiQ== | string | 签名密文 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Url】RSA公私钥生成

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-18 10:16:07

> 更新时间: 2026-01-08 14:41:01

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/getRSACert?token=eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6MSwiaWQiOjF9.kEpJQNbsm6qjsJwDV7r7628cmwutCyhA-X3Do8nfCVY

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6MSwiaWQiOjF9.kEpJQNbsm6qjsJwDV7r7628cmwutCyhA-X3Do8nfCVY | string | 是 | Token （授权检测成功后返回的） |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "生成成功",
    "data": {
        "privateKey": "http:\/\/127.0.1.7\/static\/RSACert\/Url\/app_1_auth_nathan.com\/private_key.pem",
        "publicKey": "http:\/\/127.0.1.7\/static\/RSACert\/Url\/app_1_auth_nathan.com\/public_key.pem",
        "privateKeyBase64": "http:\/\/127.0.1.7\/static\/RSACert\/Url\/app_1_auth_nathan.com\/private_key_base64.txt",
        "publicKeyBase64": "http:\/\/127.0.1.7\/static\/RSACert\/Url\/app_1_auth_nathan.com\/public_key_base64.txt",
        "RSACertZip": "http:\/\/127.0.1.7\/static\/RSACert\/Url\/app_1_auth_nathan.com\/RSACert.zip"
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 生成成功 | string | 返回文字描述 |
| data | - | object | - |
| data.privateKey | http://127.0.1.7/static/RSACert/Url/app_1_auth_nathan.com/private_key.pem | string | 私钥外链（PEM标准格式） |
| data.publicKey | http://127.0.1.7/static/RSACert/Url/app_1_auth_nathan.com/public_key.pem | string | 公钥外链（PEM标准格式） |
| data.privateKeyBase64 | http://127.0.1.7/static/RSACert/Url/app_1_auth_nathan.com/private_key_base64.txt | string | 私钥外链（Base64无换行格式） |
| data.publicKeyBase64 | http://127.0.1.7/static/RSACert/Url/app_1_auth_nathan.com/public_key_base64.txt | string | 公钥外链（Base64无换行格式） |
| data.RSACertZip | http://127.0.1.7/static/RSACert/Url/app_1_auth_nathan.com/RSACert.zip | string | 证书压缩包 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Url】RSA验证签名

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-18 10:44:21

> 更新时间: 2026-01-08 14:41:01

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/verifyRSACert

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6MSwiaWQiOjF9.kEpJQNbsm6qjsJwDV7r7628cmwutCyhA-X3Do8nfCVY | string | 是 | Token （授权检测成功后返回的） |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQIN+V0x8nPpAUCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECCntqZEfC4+KBIIEyPzZoJjHrkyr vwR/7zqEI61+2GI2zqDTobsbjGT+4N50a9yMz6w8BwXWIfrNZzU+aT2GQZOcwloU CuY/NE2iXHQIRA637y1gmT+WtzoZplpSFsOmXmNflp9sueIKuLTlu6J6X+RyoQN9 QOTSyOe2iTY0O34Vck+GVZfyFNTrWdeGQmejFlEAfCCFgJ5DYYXSxUV1YUB0tQfF Q/w8H0eOxYp03t+rE/37cwkVf0zKddSWJzi39s0nZov40TV9d2CfUolrSWWgVyB4 Oa19OkKgEA0+cvXd2hiQgGhkCnFw3uYedkaJvMxcfzkYAr/5U62698wnZYL5yTox sbosjxBXjqwft6n49IKZ6ofpKdr8jIcxgZ2wKQ28lrZeKsivGqN8O+8ums0MRHZR 4OPtpffObNegvnF2vwNNrrpi0Xnz9ZoX5nNNqAabgidhV6gnxmr2cPd33vUowL2T q4TBgNBGwasnjEC2V14kpaiHDk7CLxP7BUaOdkKdCmf/9WVNJz+3pQpvb4wx4jh0 koQDA+nUwpQJj+0UvFmZF2fd0sHmyftZ4N6cFDk1ymYFz9sRT0zWiBEDKuK6XCXv xRV88VTf65fLvdKnP94FuCeeEneeJRgtFjlXIehvtqGj2RbamSXyNdWcg1F46sku 8smIV+Pvh6VbCLLMQ8+wjzCzZmOMrAUu0BM11IFneIXWlXH9Oe/BmGAxy1ucWBnM OZpnSgvv2dkJTjCyCyt84j1YA4TttkQaXuhDsZ5Bebxl417u+xN8+JXL/6rd6xVG NHl+soxXphw75o5EcuqL+AYxaN8rRCZl9Wh9an3jcca5WFjI7a5v6UAnDii3O/nS W5CWOzEjptbKwJ+A+9V6OyvfKxDg9aD84BsMs3iMVP6b9RTT7oY54TnTlVMclreh cpZ4bn4t8a30EhSqjoJBDB2izYLajbLV/TraPCpURvS6c1HrjMt6N0wDitnJkV7N y5i22CaL5igFln8SaWORCXPBNUoFBcViWpLt2SLznEEjru0xnFStjgnnZLp3Qi3y QUxQ4oWyoOS/45VW3mUVffEx6GfAaUKG9OSpVNBoSZYPtp+y1XbLSI9PBT3KF0sp ekJ3Mti/b1+rVTgSHDuc0qm1bhyDghO/YtEly4xboHGCjPU+ILh48CNZKkEweyDR 4efsSMYm7jv4v90kEuoeP8zVf8a9FR0JBi5cG0g3s/sngpR7ffMjdaWG3G8DEV3U 3S2vppkCwdjh6ZLk4O1Ihnp+8CIRH2Fy/H/1OWQIMy1DRhn+QxLj86c7S/ILhILh o0KJbzcXoi5Fn9R4k+QYxhRzqJG2kIdRYpOhZeFogeYhu0HNsP8y8FamNXW8qaCD 6Ah8y6VqRlnGQmrqfyRqKMLAdz1sOfOg5goOwKJ4+ctiVu8dK8Cx2KSIevlrkbRt /z14ue0uTLJ3aKB47Ue9c7l9Zsktb+zxhHUBmcec3zFu8G25TFvLN0wo5Ikaeb+z 2q3//7w4XEZmk1QlWyIGvmIl75HYbEsc+JAOsG1P12ZnGO3AFXSh14+gl8wmi25v ultmEP736tHPlE6YnWuZBlDBoA5lx4aSH8STRx5cK+flHwxoRYlOxzWWIT2WyTlm pORKjX/Xx1X52yfNawzkXA== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznTRi08IqmpaxZvXT2x5 gBBqpXuj+/8ryc85w3zAO5ZG63QlAIs5+yE+jYCjJjABhQiTCWl0QWeKZxWCFUAy weXo1XV7klleohVo2hmgWFLZ+IXKEAZdS5dfHfBFYghlgZuxpP3TeUFFIRUd9GD1 d+A30SPfJ1+TbT3STFabgo/wM5pkrvmkhNgNEv1UfHksZVobT34jIJ71FnC2rjr+ tPdMa2IBTM7zZj6ktx9Qha3ZMm7jA7/1gnq0DOCVhtL80TElAc0CboLdHpWblF7H uolyA8N8ND2OFEmghUZI1imdm+oHLqVhcLuDPDcLPxSUypC3bDUnW+HiIR4oJUHO OQIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| signature | hxclkDOC5em5qbZagEolQSCbn8CJQZCB+yFl08hbc+MohvrIq2oW/8l0YvkNg++NpQdsnlsvF5jBK7fFlnDqd4nqlaDI/IVOEKpa75jYsJA9WYAStMbYC2pgeQtlkdtxCBw0TRTTzjKqmvlEdaYZ9UmNxGJp27Xda8ZXbaKbh19hnMxBDeSLh5MG/tZyjBkW+Etmg1q4Yr2/jvCW1OIjvRcGFhulFQY7Z4uB9iPHb0kKXelvi3nAd1Q1c1FCFe9b6edG7lC96dDzveeMnDgAL3pstQJd8fSOL7wve4jMYblykaRURTfLaK/NrnOnpHrsC0GwpuXGMvTJQmOzDQe4Ww== | string | 是 | 已签名内容 |
| sign_data | Nathan | string | 是 | 验签原始内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"签名验证成功","isVerified":true}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 签名验证成功 | string | 返回文字描述 |
| isVerified | true | boolean | true成功 false失败 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Url】RSA数据加密

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-19 13:46:55

> 更新时间: 2026-01-08 14:41:01

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/encryptRSACert

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6MSwiaWQiOjF9.kEpJQNbsm6qjsJwDV7r7628cmwutCyhA-X3Do8nfCVY | string | 是 | Token （授权检测成功后返回的） |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQIN+V0x8nPpAUCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECCntqZEfC4+KBIIEyPzZoJjHrkyr vwR/7zqEI61+2GI2zqDTobsbjGT+4N50a9yMz6w8BwXWIfrNZzU+aT2GQZOcwloU CuY/NE2iXHQIRA637y1gmT+WtzoZplpSFsOmXmNflp9sueIKuLTlu6J6X+RyoQN9 QOTSyOe2iTY0O34Vck+GVZfyFNTrWdeGQmejFlEAfCCFgJ5DYYXSxUV1YUB0tQfF Q/w8H0eOxYp03t+rE/37cwkVf0zKddSWJzi39s0nZov40TV9d2CfUolrSWWgVyB4 Oa19OkKgEA0+cvXd2hiQgGhkCnFw3uYedkaJvMxcfzkYAr/5U62698wnZYL5yTox sbosjxBXjqwft6n49IKZ6ofpKdr8jIcxgZ2wKQ28lrZeKsivGqN8O+8ums0MRHZR 4OPtpffObNegvnF2vwNNrrpi0Xnz9ZoX5nNNqAabgidhV6gnxmr2cPd33vUowL2T q4TBgNBGwasnjEC2V14kpaiHDk7CLxP7BUaOdkKdCmf/9WVNJz+3pQpvb4wx4jh0 koQDA+nUwpQJj+0UvFmZF2fd0sHmyftZ4N6cFDk1ymYFz9sRT0zWiBEDKuK6XCXv xRV88VTf65fLvdKnP94FuCeeEneeJRgtFjlXIehvtqGj2RbamSXyNdWcg1F46sku 8smIV+Pvh6VbCLLMQ8+wjzCzZmOMrAUu0BM11IFneIXWlXH9Oe/BmGAxy1ucWBnM OZpnSgvv2dkJTjCyCyt84j1YA4TttkQaXuhDsZ5Bebxl417u+xN8+JXL/6rd6xVG NHl+soxXphw75o5EcuqL+AYxaN8rRCZl9Wh9an3jcca5WFjI7a5v6UAnDii3O/nS W5CWOzEjptbKwJ+A+9V6OyvfKxDg9aD84BsMs3iMVP6b9RTT7oY54TnTlVMclreh cpZ4bn4t8a30EhSqjoJBDB2izYLajbLV/TraPCpURvS6c1HrjMt6N0wDitnJkV7N y5i22CaL5igFln8SaWORCXPBNUoFBcViWpLt2SLznEEjru0xnFStjgnnZLp3Qi3y QUxQ4oWyoOS/45VW3mUVffEx6GfAaUKG9OSpVNBoSZYPtp+y1XbLSI9PBT3KF0sp ekJ3Mti/b1+rVTgSHDuc0qm1bhyDghO/YtEly4xboHGCjPU+ILh48CNZKkEweyDR 4efsSMYm7jv4v90kEuoeP8zVf8a9FR0JBi5cG0g3s/sngpR7ffMjdaWG3G8DEV3U 3S2vppkCwdjh6ZLk4O1Ihnp+8CIRH2Fy/H/1OWQIMy1DRhn+QxLj86c7S/ILhILh o0KJbzcXoi5Fn9R4k+QYxhRzqJG2kIdRYpOhZeFogeYhu0HNsP8y8FamNXW8qaCD 6Ah8y6VqRlnGQmrqfyRqKMLAdz1sOfOg5goOwKJ4+ctiVu8dK8Cx2KSIevlrkbRt /z14ue0uTLJ3aKB47Ue9c7l9Zsktb+zxhHUBmcec3zFu8G25TFvLN0wo5Ikaeb+z 2q3//7w4XEZmk1QlWyIGvmIl75HYbEsc+JAOsG1P12ZnGO3AFXSh14+gl8wmi25v ultmEP736tHPlE6YnWuZBlDBoA5lx4aSH8STRx5cK+flHwxoRYlOxzWWIT2WyTlm pORKjX/Xx1X52yfNawzkXA== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznTRi08IqmpaxZvXT2x5 gBBqpXuj+/8ryc85w3zAO5ZG63QlAIs5+yE+jYCjJjABhQiTCWl0QWeKZxWCFUAy weXo1XV7klleohVo2hmgWFLZ+IXKEAZdS5dfHfBFYghlgZuxpP3TeUFFIRUd9GD1 d+A30SPfJ1+TbT3STFabgo/wM5pkrvmkhNgNEv1UfHksZVobT34jIJ71FnC2rjr+ tPdMa2IBTM7zZj6ktx9Qha3ZMm7jA7/1gnq0DOCVhtL80TElAc0CboLdHpWblF7H uolyA8N8ND2OFEmghUZI1imdm+oHLqVhcLuDPDcLPxSUypC3bDUnW+HiIR4oJUHO OQIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| encrypt_data | NathanEncode | string | 是 | 需加密的内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"加密成功","encryptedData":"fCRyTp8qO5jVpaNge8UeZEt67Ghu5nYvCO27RM0KCOBH3pfbm2H8abCrG29uLnYAs387i1\/Vyd+uaKeZG8+fN+dGhO6l0UMbQg+rX5gwqj0H99ZjkYYb8QsDs25hNGp8TkpD4lHMjp2oXIiyPsLPJhTxfwj8J2ivofiRCFiGB2lpHcltMezUS0TFL6975LNED7trE2EzLvK2wdOswsNJvObYcrSyCzzvZR5CgJGJfO2x1r3LpaUYDLbHlU7K+A3g1MllgIU0QsholqHCGxUNsEp1XLnm\/GePO0GygQCOrANyF9QcHDil1i7ePyKQaf057WjYVs0Y9FXP2gQPtgePfg=="}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 加密成功 | string | 返回文字描述 |
| encryptedData | fCRyTp8qO5jVpaNge8UeZEt67Ghu5nYvCO27RM0KCOBH3pfbm2H8abCrG29uLnYAs387i1/Vyd+uaKeZG8+fN+dGhO6l0UMbQg+rX5gwqj0H99ZjkYYb8QsDs25hNGp8TkpD4lHMjp2oXIiyPsLPJhTxfwj8J2ivofiRCFiGB2lpHcltMezUS0TFL6975LNED7trE2EzLvK2wdOswsNJvObYcrSyCzzvZR5CgJGJfO2x1r3LpaUYDLbHlU7K+A3g1MllgIU0QsholqHCGxUNsEp1XLnm/GePO0GygQCOrANyF9QcHDil1i7ePyKQaf057WjYVs0Y9FXP2gQPtgePfg== | string | 加密结果 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Url】RSA数据解密

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-19 13:46:39

> 更新时间: 2026-01-08 14:41:01

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/decryptRSACert

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6MSwiaWQiOjF9.kEpJQNbsm6qjsJwDV7r7628cmwutCyhA-X3Do8nfCVY | string | 是 | Token （授权检测成功后返回的） |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQIN+V0x8nPpAUCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECCntqZEfC4+KBIIEyPzZoJjHrkyr vwR/7zqEI61+2GI2zqDTobsbjGT+4N50a9yMz6w8BwXWIfrNZzU+aT2GQZOcwloU CuY/NE2iXHQIRA637y1gmT+WtzoZplpSFsOmXmNflp9sueIKuLTlu6J6X+RyoQN9 QOTSyOe2iTY0O34Vck+GVZfyFNTrWdeGQmejFlEAfCCFgJ5DYYXSxUV1YUB0tQfF Q/w8H0eOxYp03t+rE/37cwkVf0zKddSWJzi39s0nZov40TV9d2CfUolrSWWgVyB4 Oa19OkKgEA0+cvXd2hiQgGhkCnFw3uYedkaJvMxcfzkYAr/5U62698wnZYL5yTox sbosjxBXjqwft6n49IKZ6ofpKdr8jIcxgZ2wKQ28lrZeKsivGqN8O+8ums0MRHZR 4OPtpffObNegvnF2vwNNrrpi0Xnz9ZoX5nNNqAabgidhV6gnxmr2cPd33vUowL2T q4TBgNBGwasnjEC2V14kpaiHDk7CLxP7BUaOdkKdCmf/9WVNJz+3pQpvb4wx4jh0 koQDA+nUwpQJj+0UvFmZF2fd0sHmyftZ4N6cFDk1ymYFz9sRT0zWiBEDKuK6XCXv xRV88VTf65fLvdKnP94FuCeeEneeJRgtFjlXIehvtqGj2RbamSXyNdWcg1F46sku 8smIV+Pvh6VbCLLMQ8+wjzCzZmOMrAUu0BM11IFneIXWlXH9Oe/BmGAxy1ucWBnM OZpnSgvv2dkJTjCyCyt84j1YA4TttkQaXuhDsZ5Bebxl417u+xN8+JXL/6rd6xVG NHl+soxXphw75o5EcuqL+AYxaN8rRCZl9Wh9an3jcca5WFjI7a5v6UAnDii3O/nS W5CWOzEjptbKwJ+A+9V6OyvfKxDg9aD84BsMs3iMVP6b9RTT7oY54TnTlVMclreh cpZ4bn4t8a30EhSqjoJBDB2izYLajbLV/TraPCpURvS6c1HrjMt6N0wDitnJkV7N y5i22CaL5igFln8SaWORCXPBNUoFBcViWpLt2SLznEEjru0xnFStjgnnZLp3Qi3y QUxQ4oWyoOS/45VW3mUVffEx6GfAaUKG9OSpVNBoSZYPtp+y1XbLSI9PBT3KF0sp ekJ3Mti/b1+rVTgSHDuc0qm1bhyDghO/YtEly4xboHGCjPU+ILh48CNZKkEweyDR 4efsSMYm7jv4v90kEuoeP8zVf8a9FR0JBi5cG0g3s/sngpR7ffMjdaWG3G8DEV3U 3S2vppkCwdjh6ZLk4O1Ihnp+8CIRH2Fy/H/1OWQIMy1DRhn+QxLj86c7S/ILhILh o0KJbzcXoi5Fn9R4k+QYxhRzqJG2kIdRYpOhZeFogeYhu0HNsP8y8FamNXW8qaCD 6Ah8y6VqRlnGQmrqfyRqKMLAdz1sOfOg5goOwKJ4+ctiVu8dK8Cx2KSIevlrkbRt /z14ue0uTLJ3aKB47Ue9c7l9Zsktb+zxhHUBmcec3zFu8G25TFvLN0wo5Ikaeb+z 2q3//7w4XEZmk1QlWyIGvmIl75HYbEsc+JAOsG1P12ZnGO3AFXSh14+gl8wmi25v ultmEP736tHPlE6YnWuZBlDBoA5lx4aSH8STRx5cK+flHwxoRYlOxzWWIT2WyTlm pORKjX/Xx1X52yfNawzkXA== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznTRi08IqmpaxZvXT2x5 gBBqpXuj+/8ryc85w3zAO5ZG63QlAIs5+yE+jYCjJjABhQiTCWl0QWeKZxWCFUAy weXo1XV7klleohVo2hmgWFLZ+IXKEAZdS5dfHfBFYghlgZuxpP3TeUFFIRUd9GD1 d+A30SPfJ1+TbT3STFabgo/wM5pkrvmkhNgNEv1UfHksZVobT34jIJ71FnC2rjr+ tPdMa2IBTM7zZj6ktx9Qha3ZMm7jA7/1gnq0DOCVhtL80TElAc0CboLdHpWblF7H uolyA8N8ND2OFEmghUZI1imdm+oHLqVhcLuDPDcLPxSUypC3bDUnW+HiIR4oJUHO OQIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| decrypt_data | aLEbnBnbmhalQ+HWJv0hAvTldB8lhlvNvaegSoal+dWqvbCElrJGv49LO2sz/nK+9T17Ssbg9c7wwwKOEgDM1LhrPLg1Njvw82dQhvftzrVHdcW4Sb2L80RW+Azs08pXxSA7CcE09rO8ATiXgfbZycb3qQAb3iP9XXBMsft5B2GdlryHJX0+h1JvFBBLwzouamF7fqDTejQSY31M0AJzs6UjZtg26R2u1wNbqTO/PbNEk3XCxXkkUC6T39ZGmgyAS0MwXleUMYdVbehYPnIGbP7VKZp/dWj98r0ziF2BDm/qbcQPxqK5VzQ+ibkF+g7pBUkEi1JWmp4RGm5wC/JjKw== | string | 是 | 需解密的内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"解密成功","decryptedData":"NathanEncode"}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 解密成功 | string | 返回文字描述 |
| decryptedData | NathanEncode | string | 解密结果 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Url】获取更新包文件列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-20 18:29:15

> 更新时间: 2026-01-08 14:41:01

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/versionUpdateFile?appid=1&version=1.0&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| version | 1.0 | string | 是 | 版本号 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"更新文件信息获取成功","size":"10.52 KB","fileCount":8,"fileList":[{"name":"1.js","size":"37 B"},{"name":"MpSend.php","size":"10.13 KB"},{"name":"index.html","size":"132 B"},{"name":"app\/controller\/Index.php","size":"28 B"},{"name":"app\/controller\/Pay.php","size":"26 B"},{"name":"app\/model\/User.php","size":"47 B"},{"name":"app\/view\/index\/index.html","size":"132 B"},{"name":"public\/1.css","size":"0 B"}],"fileData":{"1.js":{"name":"1.js","extension":"js","size":"37 B","modified":"2024-09-21 10:19:25"},"MpSend.php":{"name":"MpSend.php","extension":"php","size":"10.13 KB","modified":"2024-09-09 17:03:58"},"index.html":{"name":"index.html","extension":"html","size":"132 B","modified":"2024-09-20 17:30:04"},"app":{"controller":{"Index.php":{"name":"Index.php","extension":"php","size":"28 B","modified":"2024-09-20 17:30:38"},"Pay.php":{"name":"Pay.php","extension":"php","size":"26 B","modified":"2024-09-20 17:32:14"}},"model":{"User.php":{"name":"User.php","extension":"php","size":"47 B","modified":"2024-09-20 17:40:29"}},"view":{"app":[],"index":{"index.html":{"name":"index.html","extension":"html","size":"132 B","modified":"2024-09-21 09:44:57"}}}},"config":[],"public":{"1.css":{"name":"1.css","extension":"css","size":"0 B","modified":"2024-09-20 17:30:59"}}}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 更新文件信息获取成功 | string | 返回文字描述 |
| size | 10.52 KB | string | 文件大小 |
| fileCount | 8 | number | 文件总数 个 |
| fileList | - | array | 文件列表 |
| fileList.name | 1.js | string | 文件名 |
| fileList.size | 37 B | string | 文件大小 |
| fileData | - | object | 文件数据 |
| fileData.1.js | - | object | - |
| fileData.1.js.name | 1.js | string | - |
| fileData.1.js.extension | js | string | - |
| fileData.1.js.size | 37 B | string | - |
| fileData.1.js.modified | 2024-09-21 10:19:25 | string | - |
| fileData.MpSend.php | - | object | - |
| fileData.MpSend.php.name | MpSend.php | string | 文件名 |
| fileData.MpSend.php.extension | php | string | 文件扩展名 |
| fileData.MpSend.php.size | 10.13 KB | string | 文件大小 |
| fileData.MpSend.php.modified | 2024-09-09 17:03:58 | string | 更新时间 |
| fileData.index.html | - | object | - |
| fileData.index.html.name | index.html | string | - |
| fileData.index.html.extension | html | string | - |
| fileData.index.html.size | 132 B | string | - |
| fileData.index.html.modified | 2024-09-20 17:30:04 | string | - |
| fileData.app | - | object | - |
| fileData.app.controller | - | object | - |
| fileData.app.controller.Index.php | - | object | - |
| fileData.app.controller.Index.php.name | Index.php | string | - |
| fileData.app.controller.Index.php.extension | php | string | - |
| fileData.app.controller.Index.php.size | 28 B | string | - |
| fileData.app.controller.Index.php.modified | 2024-09-20 17:30:38 | string | - |
| fileData.app.controller.Pay.php | - | object | - |
| fileData.app.controller.Pay.php.name | Pay.php | string | - |
| fileData.app.controller.Pay.php.extension | php | string | - |
| fileData.app.controller.Pay.php.size | 26 B | string | - |
| fileData.app.controller.Pay.php.modified | 2024-09-20 17:32:14 | string | - |
| fileData.app.model | - | object | - |
| fileData.app.model.User.php | - | object | - |
| fileData.app.model.User.php.name | User.php | string | - |
| fileData.app.model.User.php.extension | php | string | - |
| fileData.app.model.User.php.size | 47 B | string | - |
| fileData.app.model.User.php.modified | 2024-09-20 17:40:29 | string | - |
| fileData.app.view | - | object | - |
| fileData.app.view.app | - | array | - |
| fileData.app.view.index | - | object | - |
| fileData.app.view.index.index.html | - | object | - |
| fileData.app.view.index.index.html.name | index.html | string | - |
| fileData.app.view.index.index.html.extension | html | string | - |
| fileData.app.view.index.index.html.size | 132 B | string | - |
| fileData.app.view.index.index.html.modified | 2024-09-21 09:44:57 | string | - |
| fileData.config | - | array | - |
| fileData.public | - | object | - |
| fileData.public.1.css | - | object | - |
| fileData.public.1.css.name | 1.css | string | - |
| fileData.public.1.css.extension | css | string | - |
| fileData.public.1.css.size | 0 B | string | - |
| fileData.public.1.css.modified | 2024-09-20 17:30:59 | string | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Url】服务计费 操作加减额度

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-04-08 21:13:40

> 更新时间: 2026-01-08 14:41:01

**Token为授权检测成功后返回的，详细可见授权检测接口**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/billingControl?token=1&webkey=Nathan_Auth&billing_key=SMS&type=1&count=10

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| billing_key | SMS | string | 是 | 服务标识 您的服务类型（如：SMS） |
| type | 1 | string | 是 | 操作类型  1：加额度 2：减额度 |
| count | 10 | string | 是 | 数量 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "增加额度成功",
    "data": {
        "billing_key": "SMS",
        "old_quota": 20,
        "control_quota": "1",
        "new_quota": 21
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 增加额度成功 | string | 返回文字描述 |
| data | - | object | - |
| data.billing_key | SMS | string | 服务标识 您的服务类型（如：SMS） |
| data.old_quota | 20 | number | 原来额度数 |
| data.control_quota | 1 | string | 操作额度数 |
| data.new_quota | 21 | number | 现在额度数 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Url】服务计费 获取额度数据

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-04-08 21:14:19

> 更新时间: 2026-01-08 14:41:01

**Token为授权检测成功后返回的，详细可见授权检测接口**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/queryBilling?token=1&webkey=Nathan_Auth&billing_key=SMS

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| billing_key | SMS | string | 是 | 服务标识 您的服务类型（如：SMS） |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "查询成功",
    "data": {
        "billing_key": "SMS",
        "quota": 1,
        "create_time": "2025-04-08 17:02:45",
        "app_name": "Nathan_Auth授权系统",
        "app_id": 1
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 查询成功 | string | 返回文字描述 |
| data | - | object | - |
| data.billing_key | SMS | string | 服务标识 您的服务类型（如：SMS） |
| data.quota | 1 | number | 额度数 |
| data.create_time | 2025-04-08 17:02:45 | string | - |
| data.app_name | Nathan_Auth授权系统 | string | - |
| data.app_id | 1 | number | - |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Url】获取用户信息及权限

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-04-10 14:14:51

> 更新时间: 2026-03-02 16:07:26

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/index/getUserInfo?type=username&value=admin&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| type | username | string | 是 | 查询类型 四个类型（username，qq ，email，phone） |
| value | admin | string | 是 | 查询的内容 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "查询成功",
    "data": {
        "username": "admin",
        "qq": "2322796106",
        "email": "2322796106@qq.com",
        "phone": "17777777777",
        "loginip": "127.0.0.1",
        "logincity": "本地局域网",
        "logintime": "2024-06-09 16:11:41",
        "addtime": "2022-12-27 12:16:54",
        "money": "0.00",
        "powerData": [
            {
                "app_id": 1,
                "app_name": "Nathan_Auth授权系统",
                "power_name": "总销商",
				"app_money": 255
            },
            {
                "app_id": 2,
                "app_name": "Nathan-商城",
                "power_name": "代理商",
				"app_money": 255
            },
            {
                "app_id": 3,
                "app_name": "1",
                "power_name": "普通用户",
				"app_money": 0
            },
            {
                "app_id": 4,
                "app_name": "111122",
                "power_name": "普通用户",
				"app_money": 0
            }
        ]
    }
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Url】获取广告位列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-02 15:53:41

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/Index/getAdList?type=1&appid=1&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/Index/getAdList?apipost_id=1f89ac8f70c275

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| type | 1 | string | 是 | 广告类型 1=文本，2=视频，3=图片 |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
  "code": "1",
  "msg": "查询成功",
  "data": [
    {
      "id": "广告ID",
      "webname": "广告名称",
      "url": "广告地址",
      "jump_url": "跳转地址",
      "introduction": "广告简介",
      "appid": "应用ID",
      "date": "创建时间",
      "type": "广告类型(1文本 2视频 3图片)",
      "user_id": "用户ID(0为后台)",
      "username": "用户名或后台",
      "status": "状态(1正常 2异常)"
    }
  ]
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

## V2版

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-01-08 14:38:09

> 更新时间: 2026-01-08 14:41:50

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 调用必看【不看必错】

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-04 17:28:46

> 更新时间: 2026-03-06 15:29:07

#### NathanAuth 授权系统 V2 API 接口文档

##### 概述

**V2 API 采用 AES-256-CBC + HMAC-SHA256 加密方式，确保数据传输安全。所有接口均使用 POST 请求方式。首先要清楚V2中有两个Token，一个是应用Token（获取应用Token接口返回的），一个是授权Token（授权验证成功返回的，与V1接口相同，可调用V1相关接口）**

##### 说明

**所有V2接口都是POST请求，Body 参数放在请求体中传递，支持以下格式：**

**multipart/form-data 表单数据，支持文件上传,application/x-www-form-urlencoded 表单编码，默认表单提交格式,application/json JSON 格式，需设置 Content-Type 请求头**

**[object Object]**

**application/json JSON 格式，需设置 Content-Type 请求头**

**[object Object]**

##### 规则

###### 加密算法

**参数值请使用 AES-256-CBC + HMAC-SHA256 加密算法**

###### 密钥生成规则

**密钥由 32位大写MD5 应用密钥_你搭建的NathanAuth的网站域名（注意：应用密钥和域名之间有下划线 _ 连接）**

**[object Object]**

**示例：**

**应用密钥：NathanAuth,域名：auth.nanyinet.com,拼接字符串：NathanAuth_auth.nanyinet.com,MD5(大写)：4AAA3198E6DBDAB914B0E0DB3873E317**

**拼接字符串：NathanAuth_auth.nanyinet.com**

**[object Object]**

**MD5(大写)：4AAA3198E6DBDAB914B0E0DB3873E317**

**[object Object]**

##### PHP语言示例

###### 加密数据

**[object Object]**

###### 解密返回内容

**[object Object]**

##### 调用方法

###### 第一步：生成密钥

**根据你的应用密钥（app_key）和 NathanAuth 搭建的域名，生成加密密钥：**

**[object Object]**

###### 第二步：获取应用 Token

**调用 getToken 接口获取应用访问令牌。**

**[object Object]**

**接口地址： https://your-domain.com/api/UrlApiV2/getToken**

**[object Object]**

**请求方式： POST,请求参数：**

**[object Object]**

**请求示例：**

**[object Object]**

**返回示例：**

**[object Object]**

**解密 encrypt 字段：**

**[object Object]**

###### 第三步：调用其他接口

**其他 V2 接口需要使用 应用Token 进行认证，并对请求参数进行加密。,认证方式：Bearer Token,在 HTTP Header 中添加 Authorization 参数：**

**[object Object],[object Object]**

**参数加密：,所有请求参数（如 url、authcode、ip、version 等）都需要使用密钥进行加密后传输。**

**[object Object],[object Object],[object Object],[object Object]**

**请求示例（以 queryAuth 为例）：**

**[object Object]**

##### 完整调用流程示例

**[object Object]**

##### 重要说明

**所有接口必须使用 POST 方式请求,除 getToken 接口外，其他接口都需要在 Header 中携带 Token,请求参数需要加密后传输（除 getToken 接口的 appid 参数）,接口返回的是加密字符串（不是 JSON 格式），需要使用相同的密钥解密后才能得到 JSON 数据,密钥生成依赖于应用密钥和当前访问域名，请确保域名一致,应用Token 无过期时间限制，但建议定期更新,加密算法使用 AES-256-CBC + HMAC-SHA256，确保数据完整性和安全性**

**应用Token 无过期时间限制，但建议定期更新**

**加密算法使用 AES-256-CBC + HMAC-SHA256，确保数据完整性和安全性**

##### 错误处理

###### 应用Token 验证失败

**如果 应用Token 验证失败，接口会抛出 HTTP 401 异常，并提供详细的错误信息：**

**[object Object]**

**可能的错误原因：**

**未提供应用Token或格式错误,应用Token格式错误,应用Token中缺少appid字段,应用不存在或未配置密钥,应用Token签名验证失败,应用Token中缺少必需字段,应用Token不匹配，当前接口需要UrlApiV2,应用Token签名校验失败**

###### 请求方式错误

**如果使用非 POST 方式请求，接口会抛出 HTTP 405 异常：**

**[object Object]**

###### 参数解密失败

**如果参数解密失败，接口会返回加密的错误信息（解密后）：**

**[object Object]**

##### 常见问题

###### Q1: 为什么我的参数解密失败？

**A: 请检查以下几点：**

**密钥生成是否正确（应用密钥_域名，然后 MD5 大写）,域名是否与 NathanAuth 搭建的域名一致,加密和解密使用的密钥是否相同,数据是否在传输过程中被修改**

###### Q2: Token 验证失败怎么办？

**A: 请检查：**

**是否在 Header 中正确添加了 Authorization: Bearer {token},Token 是否正确（从 getToken 接口获取并解密）,Token 格式是否正确（Bearer 后面有空格）**

**Token 格式是否正确（Bearer 后面有空格）**

###### Q3: 接口返回的数据无法解析？

**A: V2 接口返回的是加密字符串，不是 JSON 格式。需要先使用 decrypt() 函数解密，然后再使用 json_decode() 解析。**

**[object Object],[object Object]**

**Query**

### 获取应用Token

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-04 17:25:43

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/getToken

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/getToken?apipost_id=2202dc77b0cc3d

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":1,"msg":"获取成功","encrypt":"pRQ8pjHgxoQ5KP6sTWLItVOwTz046YFjpe69igp35+kOs7V9QmtPKp5uV4EEPRKlN5ncWDXGbaPqiXOkKSGXYPA6OZBJbxLWDyKwcARoqOIfX+Q3n3bet8wvOjJMic4sHNHcMWqXsfmWDckGlVnpQeDI\/NYRUW\/Phb67MacQ5IXZdsllCSkpEmEGVPZKRn7OnaKs+sgvUIInqCDdyQkYyl53zxoeD9C0rOqNU0Xx+DN5\/MuI3j2RA9YrAZAK\/vRNU3\/H9\/pnsjkpjoVDZxzvbs3B+LA67N6eZdgmRvWvQ0KH0aNwiW\/+7Bw4DriJEwc3rnd1Bw5IKx8aG+rgVI0ZgQ=="}
```

* 失败(404)

```javascript
{"code":0,"msg":"应用ID不能为空"}
```

**Query**

### 授权查询

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-05 15:51:17

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/queryAuth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/queryAuth?apipost_id=236656edf0cff1

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| url | o7FeS36jweQIAnXKKD+ueTr4/VavnEGz9jJia6iacN0X6CtKj+GybhiR1ZtBd2d3zuXfq4jw3Drz4qeEBwcw1x+oP3H0B+9sUCbryPoZefM= | string | 是 | 授权的网站域名（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 授权验证

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-05 17:17:19

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/checkAuth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/checkAuth?apipost_id=237a08bdb0c147

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| url | o7FeS36jweQIAnXKKD+ueTr4/VavnEGz9jJia6iacN0X6CtKj+GybhiR1ZtBd2d3zuXfq4jw3Drz4qeEBwcw1x+oP3H0B+9sUCbryPoZefM= | string | 是 | 授权的网站域名（加密后传输） |
| authcode | vvUdasIhtzkG3MpdWQAN6csXpKXnNhc4i/0sgLupPmbL5/t7LWuPpCMh3DtG3wwXix6l+phG/6eVKaxHObYvykDHbK8Q4chIUxNkt5AoD4lRWAYnDPR99xPY+i3bNEmk | string | 否 | 授权的授权码（加密后传输） |
| ip | o7FeS36jweQIAnXKKD+ueTr4/VavnEGz9jJia6iacN0X6CtKj+GybhiR1ZtBd2d3zuXfq4jw3Drz4qeEBwcw1x+oP3H0B+9sUCbryPoZefM= | string | 否 | 授权的服务器IP（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 获取授权码

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-05 17:36:00

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/urlAuthCode

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/urlAuthCode?apipost_id=237e419870c26c

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1SrEuXsKmzt/j5l4H5Xz9fFKVf0xnWYDOKTxMLXBmliJ2PClywIUhrMYrDlhqptvzY/foSvI06m+9iPjqaab6DdVaGdo5zVim666yTrXZ8Dd/KIKqugoQLWWo09BQAwH6SggAG7WUraohFUnVjSWO8cvUqzX0748HMfgmrCZUVuAtprXt89omh5SjbI2677cwrSpwTcuonZs4a9Xzfo4/g== | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 获取授权所有信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-05 17:41:35

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/getAuthInfo

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/getAuthInfo?apipost_id=237f188eb0c2a1

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1SrEuXsKmzt/j5l4H5Xz9fFKVf0xnWYDOKTxMLXBmliJ2PClywIUhrMYrDlhqptvzY/foSvI06m+9iPjqaab6DdVaGdo5zVim666yTrXZ8Dd/KIKqugoQLWWo09BQAwH6SggAG7WUraohFUnVjSWO8cvUqzX0748HMfgmrCZUVuAtprXt89omh5SjbI2677cwrSpwTcuonZs4a9Xzfo4/g== | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 版本列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 09:01:50

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/versionList

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/versionList?apipost_id=24513e6430c35e

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
sowEtow7G4vWuNQRLaFHSwg0WOprnqEslvjGpa3lS6qHf8LDIWG7rUwYHHho/unf5S3MCuRKHrJNpoXfJBc5+5vZDoBPtwQfqvaWO40yLuR2jiZFs51iIyQ5Z5CD/S/6hj4JS5PPAsVxoQrfrnYqMKkcq0rzA6o13mxc5z3OVN14ArwoEqCfRA71rbQ6qa6HaFeRvHTGhxnNdd/+J5gIRDWmJK+MRVTARs5nxgp282Lmosu7+TcXdE9/6egnionXtOoBi2OGfweQWZUjdTnz5FzyuKPfxuDE4HxtY6KtndIO1NIqr2EPeQcfrrW8UcNLPKs9YamLKbJ6oj9RZWoCe86/yIWNgLzJKpI3thAKSZFYRXJNq8I7ucR9FzTPcWL65LMPa5orogXVKkYfRI+qmTIFw4B8QwGxEuFzRAGLjPOaUkpyBIKGzDkd9Vc0qRpsifBySLT2zBzTYIvfv83Nh2HUa5wjWgKrq0NEcVP4Fgdw/42uR0XP6M0NQ0Qt0JHQDQXyZ480ByuOe8Iq6vHmPgxqsNGExBf3a8slAy2iSclU4hFTzIHogSN+5oaXyMaXijIxIZV/SQ7crzzyMOnwYlVDbQUpSnGBtVVI52tymcgPj3pj17LSuBL+GWZPeMri8kQY3MHYTEwic2POHQGyz0iPhjjYImcraNNqwpOeAd40LncubK5XQ86ogTXa/mpkbLH+uZhznWjbIu7k3JRVRfrXeJi7qHGfsGOHfUwQDclcY9SWvFK5TGBcSMU6wsa+Zoo/6qIc4JDQswEVK2OzALLgxUGji2sFrQiHHWOEnAR+MDOWU8RmgTORRJhccREMQOM4jD84Gt9r3b6DZTXOp5fZuUS8lWghAtCeVgo/Z5FJz/5nyV0Y2/mJnmqOwHlVd7Ej/4QlB4N8OcTvX9Ww7Ygks/9tCyA432gGJrXUxsCDk820CYOFFHPzyyjw+ScGFOLoqjymZX2YMDgnb0A5PueffJ0ZI7cI/v6jvx7q69Y97MyR0X+9A54EjURDPWtAWEvArmokmxpLQNJZu/e+zPeudTMC/wfKlUT5GyoHXDhgCtmfLEs9OtPsQeADdkvkXTnenyVyxL5BC6lAeYAc8WYmOVSWIzuKvPUsm8A0GX94knB7pyaKmhc5Zaigqq1f
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 版本更新信息(在线更新)

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 09:13:19

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/version

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/version?apipost_id=2452adaaf0c396

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1SrEuXsKmzt/j5l4H5Xz9fFKVf0xnWYDOKTxMLXBmliJ2PClywIUhrMYrDlhqptvzY/foSvI06m+9iPjqaab6DdVaGdo5zVim666yTrXZ8Dd/KIKqugoQLWWo09BQAwH6SggAG7WUraohFUnVjSWO8cvUqzX0748HMfgmrCZUVuAtprXt89omh5SjbI2677cwrSpwTcuonZs4a9Xzfo4/g== | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |
| version | RsYGVvXzLplHfwxYvc0Ca21I9GUd19OSUw7uqzBvT7ZXPZjcXJ/tK3cpiCTw5S9rx7MoHhRPgWcRgwfN3hSiBA== | string | 是 | 应用版本号（不传或不存在则默认获取最新版）（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
sowEtow7G4vWuNQRLaFHSwg0WOprnqEslvjGpa3lS6qHf8LDIWG7rUwYHHho/unf5S3MCuRKHrJNpoXfJBc5+5vZDoBPtwQfqvaWO40yLuR2jiZFs51iIyQ5Z5CD/S/6hj4JS5PPAsVxoQrfrnYqMKkcq0rzA6o13mxc5z3OVN14ArwoEqCfRA71rbQ6qa6HaFeRvHTGhxnNdd/+J5gIRDWmJK+MRVTARs5nxgp282Lmosu7+TcXdE9/6egnionXtOoBi2OGfweQWZUjdTnz5FzyuKPfxuDE4HxtY6KtndIO1NIqr2EPeQcfrrW8UcNLPKs9YamLKbJ6oj9RZWoCe86/yIWNgLzJKpI3thAKSZFYRXJNq8I7ucR9FzTPcWL65LMPa5orogXVKkYfRI+qmTIFw4B8QwGxEuFzRAGLjPOaUkpyBIKGzDkd9Vc0qRpsifBySLT2zBzTYIvfv83Nh2HUa5wjWgKrq0NEcVP4Fgdw/42uR0XP6M0NQ0Qt0JHQDQXyZ480ByuOe8Iq6vHmPgxqsNGExBf3a8slAy2iSclU4hFTzIHogSN+5oaXyMaXijIxIZV/SQ7crzzyMOnwYlVDbQUpSnGBtVVI52tymcgPj3pj17LSuBL+GWZPeMri8kQY3MHYTEwic2POHQGyz0iPhjjYImcraNNqwpOeAd40LncubK5XQ86ogTXa/mpkbLH+uZhznWjbIu7k3JRVRfrXeJi7qHGfsGOHfUwQDclcY9SWvFK5TGBcSMU6wsa+Zoo/6qIc4JDQswEVK2OzALLgxUGji2sFrQiHHWOEnAR+MDOWU8RmgTORRJhccREMQOM4jD84Gt9r3b6DZTXOp5fZuUS8lWghAtCeVgo/Z5FJz/5nyV0Y2/mJnmqOwHlVd7Ej/4QlB4N8OcTvX9Ww7Ygks/9tCyA432gGJrXUxsCDk820CYOFFHPzyyjw+ScGFOLoqjymZX2YMDgnb0A5PueffJ0ZI7cI/v6jvx7q69Y97MyR0X+9A54EjURDPWtAWEvArmokmxpLQNJZu/e+zPeudTMC/wfKlUT5GyoHXDhgCtmfLEs9OtPsQeADdkvkXTnenyVyxL5BC6lAeYAc8WYmOVSWIzuKvPUsm8A0GX94knB7pyaKmhc5Zaigqq1f
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 查询应用自定义参数

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 09:20:29

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/queryAppParams

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/queryAppParams?apipost_id=2456741f70c4b6

**请求方式**

> POST

**Content-Type**

> none

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 版本更新文件列表信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 09:29:42

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/versionUpdateFile

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/versionUpdateFile?apipost_id=24579fb7b0c673

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| version | RsYGVvXzLplHfwxYvc0Ca21I9GUd19OSUw7uqzBvT7ZXPZjcXJ/tK3cpiCTw5S9rx7MoHhRPgWcRgwfN3hSiBA== | string | 是 | 应用版本号（不传或不存在则默认获取最新版）（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
sowEtow7G4vWuNQRLaFHSwg0WOprnqEslvjGpa3lS6qHf8LDIWG7rUwYHHho/unf5S3MCuRKHrJNpoXfJBc5+5vZDoBPtwQfqvaWO40yLuR2jiZFs51iIyQ5Z5CD/S/6hj4JS5PPAsVxoQrfrnYqMKkcq0rzA6o13mxc5z3OVN14ArwoEqCfRA71rbQ6qa6HaFeRvHTGhxnNdd/+J5gIRDWmJK+MRVTARs5nxgp282Lmosu7+TcXdE9/6egnionXtOoBi2OGfweQWZUjdTnz5FzyuKPfxuDE4HxtY6KtndIO1NIqr2EPeQcfrrW8UcNLPKs9YamLKbJ6oj9RZWoCe86/yIWNgLzJKpI3thAKSZFYRXJNq8I7ucR9FzTPcWL65LMPa5orogXVKkYfRI+qmTIFw4B8QwGxEuFzRAGLjPOaUkpyBIKGzDkd9Vc0qRpsifBySLT2zBzTYIvfv83Nh2HUa5wjWgKrq0NEcVP4Fgdw/42uR0XP6M0NQ0Qt0JHQDQXyZ480ByuOe8Iq6vHmPgxqsNGExBf3a8slAy2iSclU4hFTzIHogSN+5oaXyMaXijIxIZV/SQ7crzzyMOnwYlVDbQUpSnGBtVVI52tymcgPj3pj17LSuBL+GWZPeMri8kQY3MHYTEwic2POHQGyz0iPhjjYImcraNNqwpOeAd40LncubK5XQ86ogTXa/mpkbLH+uZhznWjbIu7k3JRVRfrXeJi7qHGfsGOHfUwQDclcY9SWvFK5TGBcSMU6wsa+Zoo/6qIc4JDQswEVK2OzALLgxUGji2sFrQiHHWOEnAR+MDOWU8RmgTORRJhccREMQOM4jD84Gt9r3b6DZTXOp5fZuUS8lWghAtCeVgo/Z5FJz/5nyV0Y2/mJnmqOwHlVd7Ej/4QlB4N8OcTvX9Ww7Ygks/9tCyA432gGJrXUxsCDk820CYOFFHPzyyjw+ScGFOLoqjymZX2YMDgnb0A5PueffJ0ZI7cI/v6jvx7q69Y97MyR0X+9A54EjURDPWtAWEvArmokmxpLQNJZu/e+zPeudTMC/wfKlUT5GyoHXDhgCtmfLEs9OtPsQeADdkvkXTnenyVyxL5BC6lAeYAc8WYmOVSWIzuKvPUsm8A0GX94knB7pyaKmhc5Zaigqq1f
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 验证授权Token是否有效

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 14:50:42

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/verifyAuthToken

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/verifyAuthToken?apipost_id=24a2145df0cf71

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1SrEuXsKmzt/j5l4H5Xz9fFKVf0xnWYDOKTxMLXBmliJ2PClywIUhrMYrDlhqptvzY/foSvI06m+9iPjqaab6DdVaGdo5zVim666yTrXZ8Dd/KIKqugoQLWWo09BQAwH6SggAG7WUraohFUnVjSWO8cvUqzX0748HMfgmrCZUVuAtprXt89omh5SjbI2677cwrSpwTcuonZs4a9Xzfo4/g== | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 服务计费 获取额度数据

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-16 15:05:27

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/queryBilling

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/queryBilling?apipost_id=31855fabb0c1e7

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1SrEuXsKmzt/j5l4H5Xz9fFKVf0xnWYDOKTxMLXBmliJ2PClywIUhrMYrDlhqptvzY/foSvI06m+9iPjqaab6DdVaGdo5zVim666yTrXZ8Dd/KIKqugoQLWWo09BQAwH6SggAG7WUraohFUnVjSWO8cvUqzX0748HMfgmrCZUVuAtprXt89omh5SjbI2677cwrSpwTcuonZs4a9Xzfo4/g== | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |
| billing_key | aFAfVrykSpPO5vym1n2Vvu+U4xkzmUihHHiTYch08lB2lsQgP2Et3YwYYTWAGrHLm4y3/1GSXNnrWexJo4nNTg== | string | 是 | 服务标识 您的服务类型（如：SMS）（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
scg0hZh14/XG7KsryyZwIntw9OkD9E70+kxZbH6CPGxdZ9wHPiubxxrY3yjFgaL9vqQHVynoq/Jo2HY8gnqQ8RmdLhemNU3kwB5ePAy/Wi+qgfzpor9sy3T/5UJTCX88Z/2xvFDjaDA2eZAlewOB7wqlsprJgt8WBRHh+9W8TtlLaImLTo/ljBSxjyh6iIMiDd3FwWcFfEVyHcaih66m8RSPEMRBm8B6fIs33g23gz3JpC7Wshx9HiavL9JAjYYwgd4LKg7zC0SY5KsseAQgBw==
```

**Query**

### 服务计费 操作加减额度

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-16 15:05:36

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/billingControl

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/billingControl?apipost_id=3185681630c215

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1SrEuXsKmzt/j5l4H5Xz9fFKVf0xnWYDOKTxMLXBmliJ2PClywIUhrMYrDlhqptvzY/foSvI06m+9iPjqaab6DdVaGdo5zVim666yTrXZ8Dd/KIKqugoQLWWo09BQAwH6SggAG7WUraohFUnVjSWO8cvUqzX0748HMfgmrCZUVuAtprXt89omh5SjbI2677cwrSpwTcuonZs4a9Xzfo4/g== | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |
| billing_key | aFAfVrykSpPO5vym1n2Vvu+U4xkzmUihHHiTYch08lB2lsQgP2Et3YwYYTWAGrHLm4y3/1GSXNnrWexJo4nNTg== | string | 是 | 服务标识 您的服务类型（如：SMS）（加密后传输） |
| type | pxNMFHEFm0N9/lWw1KELP2q7uNrlH6zHq9cD7kB6+tVd8dLO/TQhaLAcOOYsn5ScaTHOhDRuplTQU7/38Mr3Zg== | string | 是 | 操作类型  1：加额度 2：减额度（加密后传输） |
| count | nxtxtf1vPlXatP5RxExsda+Wfq9N7SlYMBR054PsMPJovvYxFwtcSa9btZctb+oKrkjAuSa7YQoKFVUlXrZK2w== | string | 是 | 数量（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
c3tnKGLsOsSQuGk4OIF4ecoZxrUpkd146ctT/qaD1L5unvpSt0Ad6GElCdHEty6cRcYASXI01k2LaWW47xxHnxpWYPURG94ITJtneR3+IP7rLXRBCCsw7k0fPQA8eVGFJ8gMtO93W+nZpWiNAtpArKfBIlKkCf5hxdT1NblfXojA2R/gQjKDS9qanaPalPZGQC5Gru4N/A1E5wp5nBss0Q==
```

**Query**

### 获取应用下所有代理信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-16 16:28:24

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/UrlApiV2/getAgentList

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/UrlApiV2/getAgentList?apipost_id=319855b4b0c6dc

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
c3tnKGLsOsSQuGk4OIF4ecoZxrUpkd146ctT/qaD1L5unvpSt0Ad6GElCdHEty6cRcYASXI01k2LaWW47xxHnxpWYPURG94ITJtneR3+IP7rLXRBCCsw7k0fPQA8eVGFJ8gMtO93W+nZpWiNAtpArKfBIlKkCf5hxdT1NblfXojA2R/gQjKDS9qanaPalPZGQC5Gru4N/A1E5wp5nBss0Q==
```

**Query**

# 机器人授权系统

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:28:50

> 更新时间: 2023-05-15 13:28:50

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## V1版

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-01-08 14:41:27

> 更新时间: 2026-01-08 14:41:27

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 【Robot】授权检测

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例,明文：http://nathan.com/api/RobotApi/query_robot?appid=1&qq=2322796106&device=123456abc,加密：http://nathan.com/api/RobotApi/query_robot?appid=2&qq=eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjIiLCJ0eXBlIjoicXEiLCJkYXRhIjoiMjMyMjc5NjEwOTk5In0.cbAaJjnqjgbLtCW7F-erPos3UVOGmDXG7iX4ZbSFAbI&device=eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjIiLCJ0eXBlIjoiZGV2aWNlIiwiZGF0YSI6IjEyMzQ1NmFiYyJ9.8PxbnVoIxNRr4EJfaYbew3N8sCyaYGyanASzeX-sVRk**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/query_robot

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | 2322796106 | string | 否 | 授权QQ （支持明文或加密，加密请调用数据加密API） |
| device | 123456abc | string | 否 | 设备码  （支持明文或加密，加密请调用数据加密API） |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "授权：2322796106 为正版授权，主人QQ为：2322796106，授权期限：永久授权",
    "data": {
        "appid": "1",
        "qq": "2322796106",
        "master": "2322796106",
        "device": "1166669",
        "authdate": "永久授权",
        "token": "eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjEiLCJxcSI6IjIzMjI3OTYxMDYiLCJpZCI6NH0.se8sbV03zuoxqYQsxrkrenCvL7WuUXB-kWMmMcFD9-A"
    }
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Robot】云黑查询

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/query_black?qq=2322796106**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/query_black

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| qq | 2322796106 | string | 是 | 需查询的QQ |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"code": "1",
	"msg": "您查询的QQ：2322796106 为系统黑名单，拉黑原因：因为白嫖，拉黑时间：2022-03-27 18:12:08"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "您查询的QQ：2322796106 非系统黑名单"
}
```

**Query**

### 【Robot】代理查询

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/query_agent?appid=1&type=robotuser&value=2322796106**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/query_agent

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| type | robotuser | string | 是 | 查询类型 四个类型（robotuser，qq ，email，phone） |
| value | 2322796106 | string | 是 | 查询的内容 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"code": "1",
	"msg": "您查询的用户为此应用的 总销商 可放心交易！"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "您查询的用户不是代理，请停止交易！"
}
```

**Query**

### 【Robot】卡密授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/create_robot?appid=1&qq=2322796106&master=2322796106&device=123456abc&email=2322796106@qq.com&phone=17777777777&key=EnrB-K441-vG4l-tVKq**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/create_robot

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | 2322796106 | string | 是 | 授权的QQ |
| master | 2322796106 | string | 是 | 授权的主人QQ |
| device | 123456abc | string | 是 | 设备码 (系统会判断此应用是否需要填写) |
| email | 2322796106@qq.com | string | 否 | 授权邮箱 |
| phone | 17777777777 | string | 否 | 授权手机号 |
| key | EnrB-K441-vG4l-tVKq | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "自助授权：2322796106成功！，授权到期时间：2024-02-19 12:49:23"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "该卡密已被使用，无法授权！"
}
```

**Query**

### 【Robot】用户添加授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://robot.nathan.com/index/user_add_auth?appid=1&qq=2322796106&master=2322796106&device=123456abc&email=2322796106@qq.com&phone=17777777777&key=OgP5U1NvBnqjVi6y**

**接口状态**

> 已完成

**接口URL**

> http(s)://机器人授权官网域名/index/user_add_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | 2322796106 | string | 是 | 授权的授权QQ |
| master | 2322796106 | string | 是 | 授权的主人QQ |
| device | 123456abc | string | 是 | 设备码 (系统会判断此应用是否需要填写) |
| email | 2322796106@qq.com | string | 否 | 授权邮箱 |
| phone | 17777777777 | string | 否 | 授权手机号 |
| key | OgP5U1NvBnqjVi6y | string | 是 | 已开通的API密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "添加授权QQ：2322796106 成功！，您授权额度剩余 0 个"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "账户不存在！"
}
```

**Query**

### 【Robot】管理员添加授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/admin_add_auth?appid=1&qq=2322796106&master=2322796106&device=123456abc&email=2322796106@qq.com&phone=17777777777&authdate=1&adminname=admin&password=123456**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/admin_add_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | 23227961061 | string | 是 | 预添加授权的授权QQ |
| master | 23227961061 | string | 是 | 预添加授权的主人QQ |
| device | 123456abc1 | string | 是 | 设备码 (系统会判断此应用是否需要填写) |
| email | 2322796106@qq.com | string | 否 | 授权邮箱 |
| phone | 17777777777 | string | 否 | 授权手机号 |
| authdate | 5 | string | 是 | 授权天数（0为永久，1为1天） |
| adminname | admin | string | 是 | 管理员用户名 |
| password | 123456 | string | 是 | 管理员密码 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
    "code": "1",
    "msg": "添加授权QQ：2322796106 成功！"
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "管理员账户不存在！"
}
```

**Query**

### 【Robot】获取应用列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/applist?webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/applist

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"id": 1,
	"app_name": "应用名称",
	"app_version": "版本号（如：1.0）",
	"app_url": "官方网址",
	"app_author": "作者名称",
	"app_qq": "客服QQ",
	"app_tips": "未授权提示",
	"app_auth_money": "授权单价",
	"frame_zip": "综合包下载地址",
	"plugin_zip": "插件包下载地址",
	"app_content": "应用介绍",
	"app_addtime": "创建时间",
	"state": "1"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Robot】获取应用信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/appinfo?appid=1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/appinfo

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"id": 1,
	"app_name": "应用名称",
	"app_version": "版本号（如：1.0）",
	"app_url": "官方网址",
	"app_author": "作者名称",
	"app_qq": "客服QQ",
	"app_tips": "未授权提示",
	"app_auth_money": "授权单价",
	"frame_zip": "综合包下载地址",
	"plugin_zip": "插件包下载地址",
	"app_content": "应用介绍",
	"app_addtime": "创建时间",
	"state": "1"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Robot】获取广告位数据

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/Adlist?webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/Adlist

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站安全密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
[
    {
        "id": 1,
        "name": "广告名称",
        "img": "广告图片地址",
        "url": "广告地址",
        "date": "添加时间",
        "state": "状态（1为正常，0为异常）"
    }
]
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Robot】获取授权信息旗下授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/master_auth?appid=1&type=master&value=2322796106&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/master_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 否 | 应用ID（不传则为全部应用） |
| type | master | string | 是 | 查询类型 三个类型（master ，email，phone） |
| value | 2322796106 | string | 是 | 查询的内容 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "查询的授权信息为 2322796106 旗下授权成功",
    "data": [
        {
            "id": 2,
            "qq": "232279610",
            "master": "2322796106",
            "device": "123456abc",
            "email": "2322796106@qq.com",
            "phone": "",
            "addtime": "2023-08-02 15:13:11",
            "username": "System",
            "appid": 1,
            "appname": "Nathan_Auth机器人",
            "authdate": "2023-08-12 00:00:00",
            "reason": null,
            "state": "1",
            "onlinedate": "暂未设置"
        }
    ]
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】更换授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:30:43

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/replace_auth?appid=1&webkey=Nathan_Auth&master=2322796106&qq=10001&new_qq=10002&device=123456&phone=17777777777&email=2322796106@qq.com**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/replace_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| master | 2322796106 | string | 是 | 主人QQ |
| qq | 10001 | string | 是 | 旧机器人授权QQ |
| new_qq | 10002 | string | 是 | 新机器人授权QQ |
| device | 123456 | string | 否 | 设备码 |
| phone | 17777777777 | string | 否 | 授权手机号 |
| email | 2322796106@qq.com | string | 否 | 授权邮箱 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "更换授权信息成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "更换失败，原因未做修改！"
}
```

**Query**

### 【Robot】获取授权上级信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 13:55:23

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/QueryAuthUpInfo?appid=1&qq=2322796106&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/QueryAuthUpInfo?appid=1&qq=2322796106&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | 2322796106 | string | 是 | 授权QQ |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "data": {
        "username": "管理员授权，无上级",
        "userqq": "管理员授权，无上级"
    }
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Robot】获取授权主人QQ

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-05-15 14:00:48

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/QueryAuthMaster?appid=1&qq=2322796106**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/QueryAuthMaster?appid=1&qq=2322796106

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | 2322796106 | string | 是 | 授权QQ |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "masterqq": "2322796106"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Robot】禁封授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-08-02 15:05:03

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/freeze_auth?appid=1&qq=1000&reason=无理由封了&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/freeze_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | 10001 | string | 是 | 授权QQ |
| reason | 无理由封了 | string | 是 | 禁封原因 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "禁封授权：qq 成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Robot】解封授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-08-02 15:05:03

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/unseal_auth?appid=1&qq=1000&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/unseal_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | qq | string | 是 | 授权qq |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "解封授权：qq 成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Robot】删除授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2023-08-02 15:05:03

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/del_auth?appid=1&qq=1000&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/del_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | qq | string | 是 | 授权QQ |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "删除授权：qq 成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Robot】创建用户

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-22 13:27:38

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/user_add?username=admin&password=123456&qq=2322796106&email=2322796106@qq.com&phone=17777777777&apistate=1&money=1&admin_name=admin&admin_password=123456**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/user_add

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| username | admin | string | 是 | 用户名 |
| password | 123456 | string | 是 | 用户密码 |
| qq | 2322796106 | string | 是 | 用户QQ |
| email | 2322796106@qq.com | string | 否 | 用户邮箱 |
| phone | 17777777777 | string | 否 | 用户手机号 |
| apistate | 1 | string | 是 | API状态 1开启 2关闭 |
| money | 1 | string | 是 | 账户余额 |
| admin_name | admin | string | 是 | 管理员账号 |
| admin_password | 123456 | string | 是 | 管理员密码 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "添加用户：admin 成功"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "该账号已存在，请更换账号！"
}
```

**Query**

### 【Robot】数据加密

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-22 13:57:28

> 更新时间: 2026-01-08 14:42:18

**请务必在后台网站设置机器人授权API Token,请务必在后台网站设置机器人授权API Token,请务必在后台网站设置机器人授权API Token,请求示例
http://nathan.com/api/RobotApi/encode_auth?appid=1&type=qq&value=2322796106&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/encode_auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| type | qq | string | 是 | 加密类型 两个类型（qq，device） |
| value | 2322796106 | string | 是 | 加密的内容 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "加密成功",
    "data": "eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoicXEiLCJkYXRhIjoiMjMyMjc5NjEwNiJ9.WPdfIRi5yQimJgqSr9B4U7OAtKs7RL5CNX_nmShPyLU"
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】检测授权所属用户状态

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-28 21:14:33

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/QueryAuthUpStatus?appid=1&qq=2322796106&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/QueryAuthUpStatus

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| qq | 2322796106 | string | 是 | 授权QQ |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "data": {
        "QQ": "2322796106",
        "UserName": "administrator",
        "statusCode": "1",
        "statusMsg": "用户状态正常"
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 获取成功 | string | - |
| data | - | object | - |
| data.QQ | 2322796106 | string | 授权QQ |
| data.UserName | administrator | string | 所属用户名 |
| data.statusCode | 1 | string | 状态码 1正常 0异常 |
| data.statusMsg | 用户状态正常 | string | 状态描述 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "错误信息提示"
}
```

**Query**

### 【Robot】应用文件下载

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-01-28 21:46:52

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/appDownUrl?appid=1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/appDownUrl

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "data": {
        "name": "Nathan_Auth机器人",
        "version": "1.0",
        "frame_zip": "https://auth.nanyinet.com/frame_zip.zip",
        "plugin_zip": "https://auth.nanyinet.com/plugin_zip.zip"
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 获取成功 | string | - |
| data | - | object | - |
| data.name | Nathan_Auth机器人 | string | 应用名称 |
| data.version | 1.0 | string | 版本号 |
| data.frame_zip | https://auth.nanyinet.com/frame_zip.zip | string | 完整包（也可自己定义） |
| data.plugin_zip | https://auth.nanyinet.com/plugin_zip.zip | string | 插件包（也可自己定义） |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】心跳开始

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-05-03 21:09:18

> 更新时间: 2026-01-08 14:42:18

**Token为授权检测成功后返回的，详细可见授权检测接口,必看说明：授权检测通过后返回个token，把这个token带到开始的接口里，记录时间，超过后台网站设置的时间范围就为下线 ，如果在这个时间内再次把token传入开始接口里调用就记录新的在线时间 ，需要手动结束的时候再把token带到结束的接口里,请务必在后台网站设置机器人授权API Token与 时间范围,请务必在后台网站设置机器人授权API Token与 时间范围,请务必在后台网站设置机器人授权API Token与 时间范围**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/onlineStart?token=1&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "添加在线状态成功",
    "data": {
        "time": 1714741664
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 添加在线状态成功 | string | - |
| data | - | object | - |
| data.time | 1714741664 | integer | 当前时间戳 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】心跳手动结束

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-05-03 21:10:00

> 更新时间: 2026-01-08 14:42:18

**Token为授权检测成功后返回的，详细可见授权检测接口,请务必在后台网站设置机器人授权API Token,请务必在后台网站设置机器人授权API Token,请务必在后台网站设置机器人授权API Token**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/onlineEnd?token=1&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "强制离线成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 强制离线成功 | string | - |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】心跳查询

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-05-03 21:11:50

> 更新时间: 2026-01-08 14:42:18

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/queryOnline?appid=1&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "获取成功！",
    "data": {
        "onlineNum": 0,
        "offlineNum": 0,
        "onlineData": [],
        "offlineData": []
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 获取成功！ | string | - |
| data | - | object | - |
| data.onlineNum | 0 | integer | 在线数量 |
| data.offlineNum | 0 | integer | 离线数量 |
| data.onlineData | - | array | 在线授权信息 |
| data.offlineData | - | array | 离线授权信息 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】查询应用自定义参数

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-05-04 12:26:51

> 更新时间: 2026-01-08 14:42:18

**Token为授权检测成功后返回的，详细可见授权检测接口,请务必在后台网站设置机器人授权API Token,请务必在后台网站设置机器人授权API Token,请务必在后台网站设置机器人授权API Token**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/QueryAppParams?token=1&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "data": {
        "key": "Nathan",
        "Auth": "自定义参数"
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 获取成功 | string | - |
| data | - | object | 自定义的参数信息 |
| data.key | Nathan | string | - |
| data.Auth | 自定义参数 | string | - |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】生成卡密

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-03-27 21:41:42

> 更新时间: 2026-01-08 14:42:18

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/createCard?webkey=Nathan_Auth&CardAct=1&count=10&appid=1&authdate=0&money=20&prefix=APP

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| CardAct | 1 | string | 是 | 卡密类型 1余额卡密 2授权卡密 |
| count | 10 | string | 是 | 生成数量 |
| appid | 1 | string | 是 | 应用ID（卡密类型为2必填） |
| authdate | 0 | string | 是 | 授权天数（卡密类型为2必填，0为永久 1为1天） |
| money | 20 | string | 是 | 卡密余额（卡密类型为1必填） |
| prefix | APP | string | 否 | 卡密自定义前缀字段（如：Nathan ,生成的卡密就是Nathan_KEY，此字段可为空） |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "生成10张卡密成功",
    "data": [
        "APP_xYQM-vIWF-uUrU-6vS2",
        "APP_Y84j-iUhW-PjG4-iKfy",
        "APP_ITRT-N9pC-343J-uo0A",
        "APP_TSUZ-Ql2g-F1RZ-uLPe",
        "APP_BxjK-ZePm-kr6D-Rr34",
        "APP_oV1V-E9lB-lyRa-7Nke",
        "APP_6TAj-5kqa-lT2L-SurY",
        "APP_s48E-VcnP-txHy-P6xc",
        "APP_OJiB-na6a-kyYt-25hO",
        "APP_kX4n-6Q0S-o9CL-d8Rk"
    ]
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 生成10张卡密成功 | string | 返回文字描述 |
| data | - | array | 生成的卡密列表 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Robot】验证授权Token是否有效

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-03-28 10:36:25

> 更新时间: 2026-01-08 14:42:18

**Token为授权检测成功后返回的，详细可见授权检测接口**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/verifyAuthToken?token=1

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "Token有效"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | Token有效 | string | 返回文字描述 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "Token无效或已过期"
}
```

**Query**

### 【Robot】RSA公私钥生成

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-19 14:14:17

> 更新时间: 2026-01-08 14:42:18

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/getRSACert?token=eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjEiLCJxcSI6IjEwMDAxIiwiaWQiOjJ9.0ReLKVp2-jkdD0HBhOyoablSH5rJ0fhfr1BWEN7qpaQ

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjEiLCJxcSI6IjEwMDAxIiwiaWQiOjJ9.0ReLKVp2-jkdD0HBhOyoablSH5rJ0fhfr1BWEN7qpaQ | string | 是 | Token （授权检测成功后返回的） |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"生成成功","data":{"privateKey":"http:\/\/127.0.1.7\/static\/RSACert\/Robot\/app_1_auth_2\/private_key.pem","publicKey":"http:\/\/127.0.1.7\/static\/RSACert\/Robot\/app_1_auth_2\/public_key.pem","privateKeyBase64":"http:\/\/127.0.1.7\/static\/RSACert\/Robot\/app_1_auth_2\/private_key_base64.txt","publicKeyBase64":"http:\/\/127.0.1.7\/static\/RSACert\/Robot\/app_1_auth_2\/public_key_base64.txt","RSACertZip":"http:\/\/127.0.1.7\/static\/RSACert\/Robot\/app_1_auth_2\/RSACert.zip"}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 生成成功 | string | 返回文字描述 |
| data | - | object | - |
| data.privateKey | http://127.0.1.7/static/RSACert/Robot/app_1_auth_2/private_key.pem | string | 私钥外链（PEM标准格式） |
| data.publicKey | http://127.0.1.7/static/RSACert/Robot/app_1_auth_2/public_key.pem | string | 公钥外链（PEM标准格式） |
| data.privateKeyBase64 | http://127.0.1.7/static/RSACert/Robot/app_1_auth_2/private_key_base64.txt | string | 私钥外链（Base64无换行格式） |
| data.publicKeyBase64 | http://127.0.1.7/static/RSACert/Robot/app_1_auth_2/public_key_base64.txt | string | 公钥外链（Base64无换行格式） |
| data.RSACertZip | http://127.0.1.7/static/RSACert/Robot/app_1_auth_2/RSACert.zip | string | 证书压缩包 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Robot】RSA生成签名

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-19 14:55:27

> 更新时间: 2026-01-08 14:42:18

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/signRSACert

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjEiLCJxcSI6IjEwMDAxIiwiaWQiOjJ9.0ReLKVp2-jkdD0HBhOyoablSH5rJ0fhfr1BWEN7qpaQ | string | 是 | Token （授权检测成功后返回的） |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI0NgfCGB3MKUCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECA+KaDNIsJnyBIIEyD8qvIuZUVmv KNmF+/IDRYn5G7tXVunGkrhzf7BfNOLZz0mD2d2QogKFAr9Y1n3hYBEEp4eUBMN/ WXOSilZv/Jkz6eXHoL38IKsIBRuuC3hAdWHW4AQAwGQQ/UFSYOWQXZelEk3wtblm dSZSdDgIDdBxjtDnrv+ECyrGKTzrg6YSd2+xRLBSY6Huk0vfrk4t8eN6QgcoXmyP A+0lUkpCAk1tt5bg0eel890oUo6/sroQboM79y5TYkhm7n0/AvWVqvtKSRngCbty 19olzJh7ugNQ0n0myOf78uTY8/NEaRrG6pBgxRUXo71cDtgCx8Go20VuBVSGRxpi nBRGjo19iP30YMrNTcDlXVOM8Dsi+jlH7xQ3rGAmhLuDH3b2fLlV8gBQsRH5Rhyw Rs2D6XScfT+jMs4qm6BN1OvgE20SjYbuak1ARzxDqRmdCmGUrWK0fDfA2hM7nD7D iraKLEx6WQwYVMicKWi+M1FFjY8xA7rCJ+/qYzs8LyRnwcpVeZjKtbZupoe7W8+a YgqKAcSvhcAzcLm6lgb76z6gOVUwYdpDEn8V2EulVpOP4t9VXNnRxdzS9Yio7aec 1TLNmnBNciqq9ReyHxnVnHo1Yb7P5RRMH2D+BrDpxwS6bwXac6VlsAroAeTfGftF ck5v0+GL6+LOH12PJUzdmA5MraaqxQkPiZ0XPr9hVlan93aNGUgtHO91hCh02KHv Mw+ADf4cYwm1a/W84z5aRT/48m6V9WZ2bPXHpsyhEj4wB5kHZ5Huzm7GLouRRSJ/ /b8o2OazEjI5an/W48z2Hp4tEBgyODyxKE9yUfMbuylx7OXu8e7ZWzW3FqkUPYuf LPS/1rNtRH36UoHNpBYjTn/ukt1rvfQMfQnh0j0NPCkzf7C5HrRXRRQ1FLFQncMj iR69tdkUo6qu3ba3Sn3enyiu758y0RKeBESw1tswO4G6nngA8il2nerdTIooepyu xPujnmGXpAtaMWbHDLVZ/+VVEGtRpgOVLAiYcIvcLOka0j1g/SZDoz92YSy3dJt8 OOWYYvE2BRYL2nOEmb95R/quRZWka2sHFlWVaDJUecqsOElhPZ1SXxJBRuqb3m9x ZeP3v76pIDTj2YxP+HqROo8x4CbxkOGWorv9jXZj8i6+C3e8unmyGkniYkkHvkMS WM7W9KvE4MuwUQ16KK5weqz8jXQ5e1ZoLki56IOi3IJgT6o5O6NrDwttDDUVa9F2 t2kWaNDRZHosRnYjPgWFi/8gRX89v4E7IvHJcCkdIVQCV8ML+CX6/6n+XAglTGoT Q6hKuFCqBhlY2hE/JEs46A5DaI837KiJRAjujdoKyeRGQXyiE9k41m12kZlfNL3X n9ZxkFq3TDcXL6EEhe4qyWD5nA/1LDnG5VVstE7p1nPsnZm8t1EU60B1W4ccETNl SjUTr+8tWAkOT4PP21lSFMZUznVpKjW7vTExYo8daEth94D+Ew4xi9NWOwm1yqD5 znbR1XAV2ZVWb5oiEJEdlMNLCvxt9uTdPJkB4YyilzZmdKiwEDHJabdyV7qCnUV2 w830sjWmk53sZl8QX3jLiSSlQpHf027WJC5m6K7rEloZuyd2bZMmJ8XTaI9fXtXj gjWgmPGpLpLcHkviA2/XLA== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtDTbFuKVdwF2SyvnARpP PBeh6qaQQ1P8kgaHlDmCSKFbEJ1dJRkh1zssF+f+1pMBt5fbHSimfTaaKEgcfpri PuNRBaGXYgitrZVMbEgqGMUqrpt5+OsMB7etHS1met1n5/wV8hbpl0r2tP2ZwzJ1 cB+tVBb78re+xwSrlhItz+/J7IMfnFITrZKiJRVgWUa9Sd9LnFPKJdQWxzTPHPeW kMLBjAtzpp3z387/Xt2fjvLaSYJtDUhem0jx77562FnE0Fw0TrggVgD0FSprWif3 fYPTF69Nsip8jUdEB+2T5zjNA/J815bK5OzHieD74sBWPpWlP9A2dX/21eraY0j8 kwIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| sign_data | NathanRobot | string | 是 | 需签名的内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"签名成功","signature":"SFtu7T\/caVivKIydlFwyahtgldrA0dyTQI+CR6HQS37wOT+cykA3AxndSrpwZcC3dqweU9uR4\/hYmyt0VLgIkPc\/Gg+QLYo19w2qVbpZVSfRn9XmXasChojkK0kpjAx+BdMWNlXO\/lZsEt3S+tHwUw7sU4ZwAikrIwuR7+qsKz2MYVCoNfJUQTKSODtTOp1P6BMnopBDQO2+3P+8X\/z2yTcIXeCw+SA23QLWM89IMXZy0W+F30JUiWxJLkORq\/1zz6bJfl7nZHxHHLA0ksWDngNFQslArvBY2SQihFN4zfBumi+BN48J+2YtfcyJUWZLjpIE\/WQO8HmKSwKySmlOiQ=="}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 签名成功 | string | 返回文字描述 |
| signature | SFtu7T/caVivKIydlFwyahtgldrA0dyTQI+CR6HQS37wOT+cykA3AxndSrpwZcC3dqweU9uR4/hYmyt0VLgIkPc/Gg+QLYo19w2qVbpZVSfRn9XmXasChojkK0kpjAx+BdMWNlXO/lZsEt3S+tHwUw7sU4ZwAikrIwuR7+qsKz2MYVCoNfJUQTKSODtTOp1P6BMnopBDQO2+3P+8X/z2yTcIXeCw+SA23QLWM89IMXZy0W+F30JUiWxJLkORq/1zz6bJfl7nZHxHHLA0ksWDngNFQslArvBY2SQihFN4zfBumi+BN48J+2YtfcyJUWZLjpIE/WQO8HmKSwKySmlOiQ== | string | 签名密文 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Robot】RSA验证签名

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-19 14:59:51

> 更新时间: 2026-01-08 14:42:18

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/verifyRSACert

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjEiLCJxcSI6IjEwMDAxIiwiaWQiOjJ9.0ReLKVp2-jkdD0HBhOyoablSH5rJ0fhfr1BWEN7qpaQ | string | 是 | Token （授权检测成功后返回的） |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI0NgfCGB3MKUCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECA+KaDNIsJnyBIIEyD8qvIuZUVmv KNmF+/IDRYn5G7tXVunGkrhzf7BfNOLZz0mD2d2QogKFAr9Y1n3hYBEEp4eUBMN/ WXOSilZv/Jkz6eXHoL38IKsIBRuuC3hAdWHW4AQAwGQQ/UFSYOWQXZelEk3wtblm dSZSdDgIDdBxjtDnrv+ECyrGKTzrg6YSd2+xRLBSY6Huk0vfrk4t8eN6QgcoXmyP A+0lUkpCAk1tt5bg0eel890oUo6/sroQboM79y5TYkhm7n0/AvWVqvtKSRngCbty 19olzJh7ugNQ0n0myOf78uTY8/NEaRrG6pBgxRUXo71cDtgCx8Go20VuBVSGRxpi nBRGjo19iP30YMrNTcDlXVOM8Dsi+jlH7xQ3rGAmhLuDH3b2fLlV8gBQsRH5Rhyw Rs2D6XScfT+jMs4qm6BN1OvgE20SjYbuak1ARzxDqRmdCmGUrWK0fDfA2hM7nD7D iraKLEx6WQwYVMicKWi+M1FFjY8xA7rCJ+/qYzs8LyRnwcpVeZjKtbZupoe7W8+a YgqKAcSvhcAzcLm6lgb76z6gOVUwYdpDEn8V2EulVpOP4t9VXNnRxdzS9Yio7aec 1TLNmnBNciqq9ReyHxnVnHo1Yb7P5RRMH2D+BrDpxwS6bwXac6VlsAroAeTfGftF ck5v0+GL6+LOH12PJUzdmA5MraaqxQkPiZ0XPr9hVlan93aNGUgtHO91hCh02KHv Mw+ADf4cYwm1a/W84z5aRT/48m6V9WZ2bPXHpsyhEj4wB5kHZ5Huzm7GLouRRSJ/ /b8o2OazEjI5an/W48z2Hp4tEBgyODyxKE9yUfMbuylx7OXu8e7ZWzW3FqkUPYuf LPS/1rNtRH36UoHNpBYjTn/ukt1rvfQMfQnh0j0NPCkzf7C5HrRXRRQ1FLFQncMj iR69tdkUo6qu3ba3Sn3enyiu758y0RKeBESw1tswO4G6nngA8il2nerdTIooepyu xPujnmGXpAtaMWbHDLVZ/+VVEGtRpgOVLAiYcIvcLOka0j1g/SZDoz92YSy3dJt8 OOWYYvE2BRYL2nOEmb95R/quRZWka2sHFlWVaDJUecqsOElhPZ1SXxJBRuqb3m9x ZeP3v76pIDTj2YxP+HqROo8x4CbxkOGWorv9jXZj8i6+C3e8unmyGkniYkkHvkMS WM7W9KvE4MuwUQ16KK5weqz8jXQ5e1ZoLki56IOi3IJgT6o5O6NrDwttDDUVa9F2 t2kWaNDRZHosRnYjPgWFi/8gRX89v4E7IvHJcCkdIVQCV8ML+CX6/6n+XAglTGoT Q6hKuFCqBhlY2hE/JEs46A5DaI837KiJRAjujdoKyeRGQXyiE9k41m12kZlfNL3X n9ZxkFq3TDcXL6EEhe4qyWD5nA/1LDnG5VVstE7p1nPsnZm8t1EU60B1W4ccETNl SjUTr+8tWAkOT4PP21lSFMZUznVpKjW7vTExYo8daEth94D+Ew4xi9NWOwm1yqD5 znbR1XAV2ZVWb5oiEJEdlMNLCvxt9uTdPJkB4YyilzZmdKiwEDHJabdyV7qCnUV2 w830sjWmk53sZl8QX3jLiSSlQpHf027WJC5m6K7rEloZuyd2bZMmJ8XTaI9fXtXj gjWgmPGpLpLcHkviA2/XLA== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtDTbFuKVdwF2SyvnARpP PBeh6qaQQ1P8kgaHlDmCSKFbEJ1dJRkh1zssF+f+1pMBt5fbHSimfTaaKEgcfpri PuNRBaGXYgitrZVMbEgqGMUqrpt5+OsMB7etHS1met1n5/wV8hbpl0r2tP2ZwzJ1 cB+tVBb78re+xwSrlhItz+/J7IMfnFITrZKiJRVgWUa9Sd9LnFPKJdQWxzTPHPeW kMLBjAtzpp3z387/Xt2fjvLaSYJtDUhem0jx77562FnE0Fw0TrggVgD0FSprWif3 fYPTF69Nsip8jUdEB+2T5zjNA/J815bK5OzHieD74sBWPpWlP9A2dX/21eraY0j8 kwIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| signature | OR2siD+VtWbGYSzQhzBHgPUwOPwAxhihZQ321FpijfRp1lzgwF50NXMgqOsH6906mt1hZjOefRjKAQPV3vI5kFOm7tIbCETropLvUPQaYLsNWplg4HomV1S9/HKlU2nVYSCu9K7RbehVsR7Udp7hQ2sRul4Cv3GFR+dyZtT63YfomlDlDA5LzwiqbKxyPH8PLe80Y2Ustk/YvIn2FqkYsjdmoFP1kgNkUyCZwb1KaTgzqxQVwS5DjamKHlbPYUGy7+Tm0A45FYU4xtxwm3SRb/cYoKoPv5WVssE1ibqT0ulzupbNBEb5LRWSdl8PlnSHnFBWUwuIi02v+6t7Pf5ytw== | string | 是 | 已签名内容 |
| sign_data | NathanRobot | string | 是 | 验签原始内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"签名验证成功","isVerified":true}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 签名验证成功 | string | 返回文字描述 |
| isVerified | true | boolean | true成功 false失败 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Robot】RSA数据加密

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-19 15:04:52

> 更新时间: 2026-01-08 14:42:18

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/encryptRSACert

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjEiLCJxcSI6IjEwMDAxIiwiaWQiOjJ9.0ReLKVp2-jkdD0HBhOyoablSH5rJ0fhfr1BWEN7qpaQ | string | 是 | Token （授权检测成功后返回的） |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI0NgfCGB3MKUCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECA+KaDNIsJnyBIIEyD8qvIuZUVmv KNmF+/IDRYn5G7tXVunGkrhzf7BfNOLZz0mD2d2QogKFAr9Y1n3hYBEEp4eUBMN/ WXOSilZv/Jkz6eXHoL38IKsIBRuuC3hAdWHW4AQAwGQQ/UFSYOWQXZelEk3wtblm dSZSdDgIDdBxjtDnrv+ECyrGKTzrg6YSd2+xRLBSY6Huk0vfrk4t8eN6QgcoXmyP A+0lUkpCAk1tt5bg0eel890oUo6/sroQboM79y5TYkhm7n0/AvWVqvtKSRngCbty 19olzJh7ugNQ0n0myOf78uTY8/NEaRrG6pBgxRUXo71cDtgCx8Go20VuBVSGRxpi nBRGjo19iP30YMrNTcDlXVOM8Dsi+jlH7xQ3rGAmhLuDH3b2fLlV8gBQsRH5Rhyw Rs2D6XScfT+jMs4qm6BN1OvgE20SjYbuak1ARzxDqRmdCmGUrWK0fDfA2hM7nD7D iraKLEx6WQwYVMicKWi+M1FFjY8xA7rCJ+/qYzs8LyRnwcpVeZjKtbZupoe7W8+a YgqKAcSvhcAzcLm6lgb76z6gOVUwYdpDEn8V2EulVpOP4t9VXNnRxdzS9Yio7aec 1TLNmnBNciqq9ReyHxnVnHo1Yb7P5RRMH2D+BrDpxwS6bwXac6VlsAroAeTfGftF ck5v0+GL6+LOH12PJUzdmA5MraaqxQkPiZ0XPr9hVlan93aNGUgtHO91hCh02KHv Mw+ADf4cYwm1a/W84z5aRT/48m6V9WZ2bPXHpsyhEj4wB5kHZ5Huzm7GLouRRSJ/ /b8o2OazEjI5an/W48z2Hp4tEBgyODyxKE9yUfMbuylx7OXu8e7ZWzW3FqkUPYuf LPS/1rNtRH36UoHNpBYjTn/ukt1rvfQMfQnh0j0NPCkzf7C5HrRXRRQ1FLFQncMj iR69tdkUo6qu3ba3Sn3enyiu758y0RKeBESw1tswO4G6nngA8il2nerdTIooepyu xPujnmGXpAtaMWbHDLVZ/+VVEGtRpgOVLAiYcIvcLOka0j1g/SZDoz92YSy3dJt8 OOWYYvE2BRYL2nOEmb95R/quRZWka2sHFlWVaDJUecqsOElhPZ1SXxJBRuqb3m9x ZeP3v76pIDTj2YxP+HqROo8x4CbxkOGWorv9jXZj8i6+C3e8unmyGkniYkkHvkMS WM7W9KvE4MuwUQ16KK5weqz8jXQ5e1ZoLki56IOi3IJgT6o5O6NrDwttDDUVa9F2 t2kWaNDRZHosRnYjPgWFi/8gRX89v4E7IvHJcCkdIVQCV8ML+CX6/6n+XAglTGoT Q6hKuFCqBhlY2hE/JEs46A5DaI837KiJRAjujdoKyeRGQXyiE9k41m12kZlfNL3X n9ZxkFq3TDcXL6EEhe4qyWD5nA/1LDnG5VVstE7p1nPsnZm8t1EU60B1W4ccETNl SjUTr+8tWAkOT4PP21lSFMZUznVpKjW7vTExYo8daEth94D+Ew4xi9NWOwm1yqD5 znbR1XAV2ZVWb5oiEJEdlMNLCvxt9uTdPJkB4YyilzZmdKiwEDHJabdyV7qCnUV2 w830sjWmk53sZl8QX3jLiSSlQpHf027WJC5m6K7rEloZuyd2bZMmJ8XTaI9fXtXj gjWgmPGpLpLcHkviA2/XLA== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtDTbFuKVdwF2SyvnARpP PBeh6qaQQ1P8kgaHlDmCSKFbEJ1dJRkh1zssF+f+1pMBt5fbHSimfTaaKEgcfpri PuNRBaGXYgitrZVMbEgqGMUqrpt5+OsMB7etHS1met1n5/wV8hbpl0r2tP2ZwzJ1 cB+tVBb78re+xwSrlhItz+/J7IMfnFITrZKiJRVgWUa9Sd9LnFPKJdQWxzTPHPeW kMLBjAtzpp3z387/Xt2fjvLaSYJtDUhem0jx77562FnE0Fw0TrggVgD0FSprWif3 fYPTF69Nsip8jUdEB+2T5zjNA/J815bK5OzHieD74sBWPpWlP9A2dX/21eraY0j8 kwIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| encrypt_data | NathanRobotEncode | string | 是 | 需加密的内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"加密成功","encryptedData":"fCRyTp8qO5jVpaNge8UeZEt67Ghu5nYvCO27RM0KCOBH3pfbm2H8abCrG29uLnYAs387i1\/Vyd+uaKeZG8+fN+dGhO6l0UMbQg+rX5gwqj0H99ZjkYYb8QsDs25hNGp8TkpD4lHMjp2oXIiyPsLPJhTxfwj8J2ivofiRCFiGB2lpHcltMezUS0TFL6975LNED7trE2EzLvK2wdOswsNJvObYcrSyCzzvZR5CgJGJfO2x1r3LpaUYDLbHlU7K+A3g1MllgIU0QsholqHCGxUNsEp1XLnm\/GePO0GygQCOrANyF9QcHDil1i7ePyKQaf057WjYVs0Y9FXP2gQPtgePfg=="}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 加密成功 | string | 返回文字描述 |
| encryptedData | fCRyTp8qO5jVpaNge8UeZEt67Ghu5nYvCO27RM0KCOBH3pfbm2H8abCrG29uLnYAs387i1/Vyd+uaKeZG8+fN+dGhO6l0UMbQg+rX5gwqj0H99ZjkYYb8QsDs25hNGp8TkpD4lHMjp2oXIiyPsLPJhTxfwj8J2ivofiRCFiGB2lpHcltMezUS0TFL6975LNED7trE2EzLvK2wdOswsNJvObYcrSyCzzvZR5CgJGJfO2x1r3LpaUYDLbHlU7K+A3g1MllgIU0QsholqHCGxUNsEp1XLnm/GePO0GygQCOrANyF9QcHDil1i7ePyKQaf057WjYVs0Y9FXP2gQPtgePfg== | string | 加密结果 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Robot】RSA数据解密

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-19 15:04:50

> 更新时间: 2026-01-08 14:42:18

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/decryptRSACert

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | eyJ0eXAiOiJKd3QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjEiLCJxcSI6IjEwMDAxIiwiaWQiOjJ9.0ReLKVp2-jkdD0HBhOyoablSH5rJ0fhfr1BWEN7qpaQ | string | 是 | Token （授权检测成功后返回的） |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI0NgfCGB3MKUCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECA+KaDNIsJnyBIIEyD8qvIuZUVmv KNmF+/IDRYn5G7tXVunGkrhzf7BfNOLZz0mD2d2QogKFAr9Y1n3hYBEEp4eUBMN/ WXOSilZv/Jkz6eXHoL38IKsIBRuuC3hAdWHW4AQAwGQQ/UFSYOWQXZelEk3wtblm dSZSdDgIDdBxjtDnrv+ECyrGKTzrg6YSd2+xRLBSY6Huk0vfrk4t8eN6QgcoXmyP A+0lUkpCAk1tt5bg0eel890oUo6/sroQboM79y5TYkhm7n0/AvWVqvtKSRngCbty 19olzJh7ugNQ0n0myOf78uTY8/NEaRrG6pBgxRUXo71cDtgCx8Go20VuBVSGRxpi nBRGjo19iP30YMrNTcDlXVOM8Dsi+jlH7xQ3rGAmhLuDH3b2fLlV8gBQsRH5Rhyw Rs2D6XScfT+jMs4qm6BN1OvgE20SjYbuak1ARzxDqRmdCmGUrWK0fDfA2hM7nD7D iraKLEx6WQwYVMicKWi+M1FFjY8xA7rCJ+/qYzs8LyRnwcpVeZjKtbZupoe7W8+a YgqKAcSvhcAzcLm6lgb76z6gOVUwYdpDEn8V2EulVpOP4t9VXNnRxdzS9Yio7aec 1TLNmnBNciqq9ReyHxnVnHo1Yb7P5RRMH2D+BrDpxwS6bwXac6VlsAroAeTfGftF ck5v0+GL6+LOH12PJUzdmA5MraaqxQkPiZ0XPr9hVlan93aNGUgtHO91hCh02KHv Mw+ADf4cYwm1a/W84z5aRT/48m6V9WZ2bPXHpsyhEj4wB5kHZ5Huzm7GLouRRSJ/ /b8o2OazEjI5an/W48z2Hp4tEBgyODyxKE9yUfMbuylx7OXu8e7ZWzW3FqkUPYuf LPS/1rNtRH36UoHNpBYjTn/ukt1rvfQMfQnh0j0NPCkzf7C5HrRXRRQ1FLFQncMj iR69tdkUo6qu3ba3Sn3enyiu758y0RKeBESw1tswO4G6nngA8il2nerdTIooepyu xPujnmGXpAtaMWbHDLVZ/+VVEGtRpgOVLAiYcIvcLOka0j1g/SZDoz92YSy3dJt8 OOWYYvE2BRYL2nOEmb95R/quRZWka2sHFlWVaDJUecqsOElhPZ1SXxJBRuqb3m9x ZeP3v76pIDTj2YxP+HqROo8x4CbxkOGWorv9jXZj8i6+C3e8unmyGkniYkkHvkMS WM7W9KvE4MuwUQ16KK5weqz8jXQ5e1ZoLki56IOi3IJgT6o5O6NrDwttDDUVa9F2 t2kWaNDRZHosRnYjPgWFi/8gRX89v4E7IvHJcCkdIVQCV8ML+CX6/6n+XAglTGoT Q6hKuFCqBhlY2hE/JEs46A5DaI837KiJRAjujdoKyeRGQXyiE9k41m12kZlfNL3X n9ZxkFq3TDcXL6EEhe4qyWD5nA/1LDnG5VVstE7p1nPsnZm8t1EU60B1W4ccETNl SjUTr+8tWAkOT4PP21lSFMZUznVpKjW7vTExYo8daEth94D+Ew4xi9NWOwm1yqD5 znbR1XAV2ZVWb5oiEJEdlMNLCvxt9uTdPJkB4YyilzZmdKiwEDHJabdyV7qCnUV2 w830sjWmk53sZl8QX3jLiSSlQpHf027WJC5m6K7rEloZuyd2bZMmJ8XTaI9fXtXj gjWgmPGpLpLcHkviA2/XLA== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtDTbFuKVdwF2SyvnARpP PBeh6qaQQ1P8kgaHlDmCSKFbEJ1dJRkh1zssF+f+1pMBt5fbHSimfTaaKEgcfpri PuNRBaGXYgitrZVMbEgqGMUqrpt5+OsMB7etHS1met1n5/wV8hbpl0r2tP2ZwzJ1 cB+tVBb78re+xwSrlhItz+/J7IMfnFITrZKiJRVgWUa9Sd9LnFPKJdQWxzTPHPeW kMLBjAtzpp3z387/Xt2fjvLaSYJtDUhem0jx77562FnE0Fw0TrggVgD0FSprWif3 fYPTF69Nsip8jUdEB+2T5zjNA/J815bK5OzHieD74sBWPpWlP9A2dX/21eraY0j8 kwIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| decrypt_data | VWmbUnlsJgk8JnN9uWlzqPpegLicjAl7sxeKcx9n0nCnZvrOF8+lmomga3BLLlaW8N5Hb4tqe/WjxO9JSxOFm7oHYuEIGSoWNCvADfL1dRUc3HtNsSUGEhkCCN/T2oUPlcJLIbPkO1K0xBDNRqzIgTWZJoqreorftXXHmCIEKsfn9/QEkaEsEFfICr8V+1e/X3+4mdiaubpuDYhTHsFGxAOPSk116pKv6U8t+kKyj/VpFSmIbg47Vgkj26CeXG+VLpk+OEehw59kvSLswf8k40A1/0LNu7ajG8riv4SrJVCgwGhqoSlt6yA0NznMz88JlETW4bzoFyfe0OksFQtYOw== | string | 是 | 需解密的内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"解密成功","decryptedData":"NathanRobotEncode"}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 解密成功 | string | 返回文字描述 |
| decryptedData | NathanRobotEncode | string | 解密结果 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Robot】获取应用公告

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-21 11:07:36

> 更新时间: 2026-01-08 14:42:18

**请求示例
http://nathan.com/api/RobotApi/notice?appid=1&webkey=Nathan_Auth**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/notice?appid=1&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "获取成功",
    "data": [
        {
            "id": 1,
            "title": "公告标题",
            "content": "公告内容",
            "username": "创建者",
            "appid": 1,
            "appname": "我的系统",
            "time": "2024-00-00",
            "state": "1"
        }
    ]
}
```

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "网站安全密钥错误，无法操作！"
}
```

**Query**

### 【Robot】服务计费 操作加减额度

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-04-09 18:27:05

> 更新时间: 2026-01-08 14:42:18

**Token为授权检测成功后返回的，详细可见授权检测接口**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/billingControl?token=1&webkey=Nathan_Auth&billing_key=SMS&type=1&count=10

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| billing_key | SMS | string | 是 | 服务标识 您的服务类型（如：SMS） |
| type | 1 | string | 是 | 操作类型  1：加额度 2：减额度 |
| count | 10 | string | 是 | 数量 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "增加额度成功",
    "data": {
        "billing_key": "SMS",
        "old_quota": 20,
        "control_quota": "1",
        "new_quota": 21
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 增加额度成功 | string | 返回文字描述 |
| data | - | object | - |
| data.billing_key | SMS | string | 服务标识 您的服务类型（如：SMS） |
| data.old_quota | 20 | number | 原来额度数 |
| data.control_quota | 1 | string | 操作额度数 |
| data.new_quota | 21 | number | 现在额度数 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】服务计费 获取额度数据

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-04-09 18:27:10

> 更新时间: 2026-01-08 14:42:18

**Token为授权检测成功后返回的，详细可见授权检测接口**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/queryBilling?token=1&webkey=Nathan_Auth&billing_key=SMS

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 1 | string | 是 | Token （授权检测成功后返回的） |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| billing_key | SMS | string | 是 | 服务标识 您的服务类型（如：SMS） |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "查询成功",
    "data": {
        "billing_key": "SMS",
        "quota": 1,
        "create_time": "2025-04-08 17:02:45",
        "app_name": "Nathan_Auth授权系统",
        "app_id": 1
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 查询成功 | string | 返回文字描述 |
| data | - | object | - |
| data.billing_key | SMS | string | 服务标识 您的服务类型（如：SMS） |
| data.quota | 1 | number | 额度数 |
| data.create_time | 2025-04-08 17:02:45 | string | - |
| data.app_name | Nathan_Auth授权系统 | string | - |
| data.app_id | 1 | number | - |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】获取用户信息及权限

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-04-10 14:36:39

> 更新时间: 2026-03-02 16:07:03

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/getUserInfo?type=robotuser&value=admin&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| type | robotuser | string | 是 | 查询类型 四个类型（robotuser，qq ，email，phone） |
| value | admin | string | 是 | 查询的内容 |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "查询成功",
    "data": {
        "username": "admin",
        "qq": "2322796106",
        "email": "2322796106@qq.com",
        "phone": "17777777777",
        "loginip": "127.0.0.1",
        "logincity": "本地局域网",
        "logintime": "2024-06-09 16:11:41",
        "addtime": "2022-12-27 12:16:54",
        "money": "0.00",
        "powerData": [
            {
                "app_id": 1,
                "app_name": "Nathan_Auth授权系统",
                "power_name": "总销商",
				"app_money": 255
            },
            {
                "app_id": 2,
                "app_name": "Nathan-商城",
                "power_name": "代理商",
				"app_money": 255
            },
            {
                "app_id": 3,
                "app_name": "1",
                "power_name": "普通用户",
				"app_money": 0
            },
            {
                "app_id": 4,
                "app_name": "111122",
                "power_name": "普通用户",
				"app_money": 0
            }
        ]
    }
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Robot】获取广告位列表

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-02 15:55:09

> 更新时间: 2026-03-25 09:30:26

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/RobotApi/getAdList?type=1&appid=1&webkey=Nathan_Auth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApi/getAdList?apipost_id=1f8a6c49f0c300

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| type | 1 | string | 是 | 广告类型 1=文本，2=视频，3=图片 |
| appid | 1 | string | 是 | 应用ID |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
  "code": "1",
  "msg": "查询成功",
  "data": [
    {
      "id": "广告ID",
      "webname": "广告名称",
      "url": "广告地址",
      "jump_url": "跳转地址",
      "introduction": "广告简介",
      "appid": "应用ID",
      "date": "创建时间",
      "type": "广告类型(1文本 2视频 3图片)",
      "user_id": "用户ID(0为后台)",
      "username": "用户名或后台",
      "status": "状态(1正常 2异常)"
    }
  ]
}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

## V2版

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-01-08 14:41:37

> 更新时间: 2026-01-08 14:41:37

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 调用必看【不看必错】

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 09:39:45

> 更新时间: 2026-03-06 15:28:57

#### NathanAuth 授权系统 V2 API 接口文档

##### 概述

**V2 API 采用 AES-256-CBC + HMAC-SHA256 加密方式，确保数据传输安全。所有接口均使用 POST 请求方式。首先要清楚V2中有两个Token，一个是应用Token（获取应用Token接口返回的），一个是授权Token（授权验证成功返回的，与V1接口相同，可调用V1相关接口）**

##### 说明

**所有V2接口都是POST请求，Body 参数放在请求体中传递，支持以下格式：**

**multipart/form-data 表单数据，支持文件上传,application/x-www-form-urlencoded 表单编码，默认表单提交格式,application/json JSON 格式，需设置 Content-Type 请求头**

**[object Object]**

**application/json JSON 格式，需设置 Content-Type 请求头**

**[object Object]**

##### 规则

###### 加密算法

**参数值请使用 AES-256-CBC + HMAC-SHA256 加密算法**

###### 密钥生成规则

**密钥由 32位大写MD5 应用密钥_你搭建的NathanAuth的网站域名（注意：应用密钥和域名之间有下划线 _ 连接）**

**[object Object]**

**示例：**

**应用密钥：NathanAuth,域名：auth.nanyinet.com,拼接字符串：NathanAuth_auth.nanyinet.com,MD5(大写)：4AAA3198E6DBDAB914B0E0DB3873E317**

**拼接字符串：NathanAuth_auth.nanyinet.com**

**[object Object]**

**MD5(大写)：4AAA3198E6DBDAB914B0E0DB3873E317**

**[object Object]**

##### PHP语言示例

###### 加密数据

**[object Object]**

###### 解密返回内容

**[object Object]**

##### 调用方法

###### 第一步：生成密钥

**根据你的应用密钥（app_key）和 NathanAuth 搭建的域名，生成加密密钥：**

**[object Object]**

###### 第二步：获取应用 Token

**调用 getToken 接口获取应用访问令牌。**

**[object Object]**

**接口地址： http://127.0.0.1/api/RobotApiV2/getToken**

**[object Object]**

**请求方式： POST,请求参数：**

**[object Object]**

**请求示例：**

**[object Object]**

**返回示例：**

**[object Object]**

**解密 encrypt 字段：**

**[object Object]**

###### 第三步：调用其他接口

**其他 V2 接口需要使用 应用Token 进行认证，并对请求参数进行加密。,认证方式：Bearer Token,在 HTTP Header 中添加 Authorization 参数：**

**[object Object],[object Object]**

**参数加密：,所有请求参数（如 qq、device 等）都需要使用密钥进行加密后传输。**

**[object Object],[object Object]**

**请求示例（以 queryRobot 为例）：**

**[object Object]**

##### 完整调用流程示例

**[object Object]**

##### 重要说明

**所有接口必须使用 POST 方式请求,除 getToken 接口外，其他接口都需要在 Header 中携带 Token,请求参数需要加密后传输（除 getToken 接口的 appid 参数）,接口返回的是加密字符串（不是 JSON 格式），需要使用相同的密钥解密后才能得到 JSON 数据,密钥生成依赖于应用密钥和当前访问域名，请确保域名一致,应用Token 无过期时间限制，但建议定期更新,加密算法使用 AES-256-CBC + HMAC-SHA256，确保数据完整性和安全性**

**应用Token 无过期时间限制，但建议定期更新**

**加密算法使用 AES-256-CBC + HMAC-SHA256，确保数据完整性和安全性**

##### 错误处理

###### 应用Token 验证失败

**如果 应用Token 验证失败，接口会抛出 HTTP 401 异常，并提供详细的错误信息：**

**[object Object]**

**可能的错误原因：**

**未提供应用Token或格式错误,应用Token格式错误,应用Token中缺少appid字段,应用不存在或未配置密钥,应用Token签名验证失败,应用Token中缺少必需字段,应用Token不匹配，当前接口需要RobotApiV2,应用Token签名校验失败**

###### 请求方式错误

**如果使用非 POST 方式请求，接口会抛出 HTTP 405 异常：**

**[object Object]**

###### 参数解密失败

**如果参数解密失败，接口会返回加密的错误信息（解密后）：**

**[object Object]**

##### 常见问题

###### Q1: 为什么我的参数解密失败？

**A: 请检查以下几点：**

**密钥生成是否正确（应用密钥_域名，然后 MD5 大写）,域名是否与 NathanAuth 搭建的域名一致,加密和解密使用的密钥是否相同,数据是否在传输过程中被修改**

###### Q2: Token 验证失败怎么办？

**A: 请检查：**

**是否在 Header 中正确添加了 Authorization: Bearer {token},Token 是否正确（从 getToken 接口获取并解密）,Token 格式是否正确（Bearer 后面有空格）**

**Token 格式是否正确（Bearer 后面有空格）**

###### Q3: 接口返回的数据无法解析？

**A: V2 接口返回的是加密字符串，不是 JSON 格式。需要先使用 decrypt() 函数解密，然后再使用 json_decode() 解析。**

**[object Object],[object Object]**

**Query**

### 获取应用Token

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 11:14:29

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/getToken

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/getToken?apipost_id=247096ef30c7c8

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":1,"msg":"获取成功","encrypt":"pRQ8pjHgxoQ5KP6sTWLItVOwTz046YFjpe69igp35+kOs7V9QmtPKp5uV4EEPRKlN5ncWDXGbaPqiXOkKSGXYPA6OZBJbxLWDyKwcARoqOIfX+Q3n3bet8wvOjJMic4sHNHcMWqXsfmWDckGlVnpQeDI\/NYRUW\/Phb67MacQ5IXZdsllCSkpEmEGVPZKRn7OnaKs+sgvUIInqCDdyQkYyl53zxoeD9C0rOqNU0Xx+DN5\/MuI3j2RA9YrAZAK\/vRNU3\/H9\/pnsjkpjoVDZxzvbs3B+LA67N6eZdgmRvWvQ0KH0aNwiW\/+7Bw4DriJEwc3rnd1Bw5IKx8aG+rgVI0ZgQ=="}
```

* 失败(404)

```javascript
{"code":0,"msg":"应用ID不能为空"}
```

**Query**

### 授权验证

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-08-16 10:37:12

> 更新时间: 2026-03-27 20:41:46

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/checkAuth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/checkAuth?apipost_id=205584b3f84086

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| qq | 3YzYJPQQipQE3Vx1Z0i8f1O07/r791w0tbm6FQ4+Z0nEgpYj/pfi4NRJC65JjrDoGs+teGQbv9N/TG822qPLkw== | string | 否 | 授权QQ（加密后传输） |
| device | mSRj7djSEga1JYMTp9js11WjTMRwypnh35UcuU706VyfbZcqc9CtCHPg9Z+ROyVMZQ8ULw0SXi9nNsD0BXjG7w== | string | 否 | 设备码（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
HEsVk3VvD4Mn/hnEHSImu/VUIuAXOojxvTdBwx2L+VdOn9n1IDGoAUKjCQMTjPlOFuJz0fQHDq0fpmKmaNK3T6HltspWd/bQ4rwzdDGoAzoe4ByHtCWzIET8vW/aw+uBIYkyLz6X+g8jD15L8ozJGDFbEcLpGv8JAJBs4yY4uHQNXrZpgzN8We7rcjuFLUlTFeGiJfNha++kJY+fSBet6K3ZVzCHV3JBgmteFuY75jRbr+Bk2lUz0xB7hIlVNvxeIUF25UN+DMNKCkGG0mYo+Tnj9VJ7SvqBtmdBjVVAPU9CiF29ZYj8L48cUS/1nPNCVoMQQOzMAU4eAJKiLcttoJOOt4MvEshNPXaRXNHqDLauZZc/zN//GbX/DA+sf4HtZd21EvXCpzDRPGOABP9RvZC0hO0n7UAB2XGtPS0iUMRrgNVNw6+LCgyR3MA/tonbsV/9vAaioC2cqvuywfVcClPHfCY90XgXWlYte//qitcdhNcIhT/cjMi65tOs0zriIVuzQlyACKdAaOg9EFVR/bYzeYRMgd8+EE2qoGoyd6h1wNx3k0N/acIorrS6RR3F
```

* 失败(404)

```javascript
HZ6NkShnVAvvvN0I4OGsYU7DHwqBXg8wSThJUFQ3b7uI7Vx2smc0KnXtmHeL78WbKJYOCt7hH9E0pi85NMA57aAWgKXL50rOQ7y590nlp/yB1FQzDMmVjPqoCkjkc/YCMgAtPdgPi0gf0FDlXKu7+03YgoTcOKin+YMxf+kRiWldTDc3qvF+8FWbrVpzA62XGWoQR7VcUgG3/d1AL4IlPmPic03atcjQwwhDb4q+dXDcX4V/Nv4qMOufeXsiFZECVObjdZLEPG/68a28P5q9ar7Q7YU9kamBy8o2NjRsKhsQ00cO/PIu7S7H8prhCGZ0okzFbCiWQZANBsTtPbJzy9lszJOzenZxIwb1z6dE/KkjAIKehbuiP6WQvfhzZRwnfsPpbxGIDnAMMfq4OU96w5bc7f6wGYu6bT6QNXVRTiIQaBt1dI59ZWudsG/qmpAJ54hdIcQ4TnYh8GYZ7XI1s7a3uqCkrqlZQuIIKOH2S9aIFSFDC4q3MyP+2GjciOT7
```

**Query**

### 查询应用自定义参数

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 14:10:02

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/queryAppParams

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/queryAppParams?apipost_id=2498c54a30cb9e

**请求方式**

> POST

**Content-Type**

> none

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 验证授权Token是否有效

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 14:21:10

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/verifyAuthToken

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/verifyAuthToken?apipost_id=249b522670cd07

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 0wNMDM+6P3sn0y85Ki30odx7Ha/9TNUtJfsvcG8Ic0jrusW2xBHDPOTqgmDK0P5lg0gJwKftrn2fZ4NRHSAeCuMcKdXpkrJHoTNccBY14JsBqB5znh2jSulZx50tOcdqXYtiqDOqoDOETkwIHCGkgvUV5ZyNvfI9PtH83+lyDD3pInMcWjWZhk6HQddIsei8BRfGnEZ3HEZKfeYaWrgWhKaaPhEK/XGDR8aG5CpNOv67djQ7REPo+oFgoYIiWG/V | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 心跳开始

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 14:27:48

> 更新时间: 2026-04-03 14:10:41

**Token为授权检测成功后返回的，详细可见授权检测接口,必看说明：授权检测通过后返回个token，把这个token带到开始的接口里，记录时间，超过后台网站设置的时间范围就为下线 ，如果在这个时间内再次把token传入开始接口里调用就记录新的在线时间 ，需要手动结束的时候再把token带到结束的接口里,请务必在后台网站设置机器人授权API Token与 时间范围,请务必在后台网站设置机器人授权API Token与 时间范围,请务必在后台网站设置机器人授权API Token与 时间范围**

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/onlineStart

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/onlineStart?apipost_id=249cbbbdb0cdc5

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 0wNMDM+6P3sn0y85Ki30odx7Ha/9TNUtJfsvcG8Ic0jrusW2xBHDPOTqgmDK0P5lg0gJwKftrn2fZ4NRHSAeCuMcKdXpkrJHoTNccBY14JsBqB5znh2jSulZx50tOcdqXYtiqDOqoDOETkwIHCGkgvUV5ZyNvfI9PtH83+lyDD3pInMcWjWZhk6HQddIsei8BRfGnEZ3HEZKfeYaWrgWhKaaPhEK/XGDR8aG5CpNOv67djQ7REPo+oFgoYIiWG/V | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 心跳手动结束

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 14:28:27

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/onlineEnd

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/onlineEnd?apipost_id=249cefd230ce50

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 0wNMDM+6P3sn0y85Ki30odx7Ha/9TNUtJfsvcG8Ic0jrusW2xBHDPOTqgmDK0P5lg0gJwKftrn2fZ4NRHSAeCuMcKdXpkrJHoTNccBY14JsBqB5znh2jSulZx50tOcdqXYtiqDOqoDOETkwIHCGkgvUV5ZyNvfI9PtH83+lyDD3pInMcWjWZhk6HQddIsei8BRfGnEZ3HEZKfeYaWrgWhKaaPhEK/XGDR8aG5CpNOv67djQ7REPo+oFgoYIiWG/V | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 心跳查询

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-06 14:28:43

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/queryOnline

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/queryOnline?apipost_id=249d000270ce7d

**请求方式**

> POST

**Content-Type**

> none

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

* 失败(404)

```javascript
6FXSoBjfm7aUNKazlNC16EIheiTi/lM/eexVyQFkNfozSpIaoTGJo4vtYc59HzuROx7vUECnX50ol6qsEQcOMpZz7xr4Ge/ue9gXEccMDVVbkeFGrUNrmMloF+hIv9pr
```

**Query**

### 服务计费 操作加减额度

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-16 15:20:50

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/billingControl

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/billingControl?apipost_id=3188e50eb0c556

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 0wNMDM+6P3sn0y85Ki30odx7Ha/9TNUtJfsvcG8Ic0jrusW2xBHDPOTqgmDK0P5lg0gJwKftrn2fZ4NRHSAeCuMcKdXpkrJHoTNccBY14JsBqB5znh2jSulZx50tOcdqXYtiqDOqoDOETkwIHCGkgvUV5ZyNvfI9PtH83+lyDD3pInMcWjWZhk6HQddIsei8BRfGnEZ3HEZKfeYaWrgWhKaaPhEK/XGDR8aG5CpNOv67djQ7REPo+oFgoYIiWG/V | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |
| billing_key | Fy3J+CAQI3MV8ULmW9LfID4XyN1ZqNcdXAHolWbz/gqN5ZAT0kLMJiSb0ieCsl6xeYOv1Pq3WFp+KBCRwHtWaQ== | string | 是 | 服务标识 您的服务类型（如：SMS）（加密后传输） |
| type | E2fpxbKNNn1DMwxfAy531sqVANBVRNlsAH8865UGxDQlOLeZVSIwmLxEXTuGyJ4/qEUdmcKwCR+cESQIm7nKPw== | string | 是 | 操作类型  1：加额度 2：减额度（加密后传输） |
| count | i2vGWGt7L3ID5G+IeUdjRiA8OTqhExiI7pZlokttTTC1CnSMSiRJdKEyLsklj3DC4dY51J8JLRzc5J8mrG0W+w== | string | 是 | 数量（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
c3tnKGLsOsSQuGk4OIF4ecoZxrUpkd146ctT/qaD1L5unvpSt0Ad6GElCdHEty6cRcYASXI01k2LaWW47xxHnxpWYPURG94ITJtneR3+IP7rLXRBCCsw7k0fPQA8eVGFJ8gMtO93W+nZpWiNAtpArKfBIlKkCf5hxdT1NblfXojA2R/gQjKDS9qanaPalPZGQC5Gru4N/A1E5wp5nBss0Q==
```

**Query**

### 服务计费 获取额度数据

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-16 15:20:42

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/queryBilling

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/queryBilling?apipost_id=3188dd5ef0c554

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 0wNMDM+6P3sn0y85Ki30odx7Ha/9TNUtJfsvcG8Ic0jrusW2xBHDPOTqgmDK0P5lg0gJwKftrn2fZ4NRHSAeCuMcKdXpkrJHoTNccBY14JsBqB5znh2jSulZx50tOcdqXYtiqDOqoDOETkwIHCGkgvUV5ZyNvfI9PtH83+lyDD3pInMcWjWZhk6HQddIsei8BRfGnEZ3HEZKfeYaWrgWhKaaPhEK/XGDR8aG5CpNOv67djQ7REPo+oFgoYIiWG/V | string | 是 | 授权Token，授权验证成功后返回的token（加密后传输） |
| billing_key | Fy3J+CAQI3MV8ULmW9LfID4XyN1ZqNcdXAHolWbz/gqN5ZAT0kLMJiSb0ieCsl6xeYOv1Pq3WFp+KBCRwHtWaQ== | string | 是 | 服务标识 您的服务类型（如：SMS）（加密后传输） |

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
scg0hZh14/XG7KsryyZwIntw9OkD9E70+kxZbH6CPGxdZ9wHPiubxxrY3yjFgaL9vqQHVynoq/Jo2HY8gnqQ8RmdLhemNU3kwB5ePAy/Wi+qgfzpor9sy3T/5UJTCX88Z/2xvFDjaDA2eZAlewOB7wqlsprJgt8WBRHh+9W8TtlLaImLTo/ljBSxjyh6iIMiDd3FwWcFfEVyHcaih66m8RSPEMRBm8B6fIs33g23gz3JpC7Wshx9HiavL9JAjYYwgd4LKg7zC0SY5KsseAQgBw==
```

**Query**

### 获取应用下所有代理信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-16 17:44:29

> 更新时间: 2026-03-25 09:21:00

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/RobotApiV2/getAgentList

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/RobotApiV2/getAgentList?apipost_id=31a9c04e30c745

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> Bearer Token

> 在Header添加参数 Authorization，其值为在Bearer之后拼接空格和访问令牌

> Authorization: Bearer your_access_token

**响应示例**

* 成功(200)

```javascript
c3tnKGLsOsSQuGk4OIF4ecoZxrUpkd146ctT/qaD1L5unvpSt0Ad6GElCdHEty6cRcYASXI01k2LaWW47xxHnxpWYPURG94ITJtneR3+IP7rLXRBCCsw7k0fPQA8eVGFJ8gMtO93W+nZpWiNAtpArKfBIlKkCf5hxdT1NblfXojA2R/gQjKDS9qanaPalPZGQC5Gru4N/A1E5wp5nBss0Q==
```

**Query**

# 软件验证系统

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-25 15:06:55

> 更新时间: 2024-09-25 15:06:55

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## V1版

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-01-08 14:42:34

> 更新时间: 2026-01-08 14:42:34

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 【Software】操作加减授权使用次数

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-08-13 17:01:27

> 更新时间: 2026-01-08 14:42:52

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/authControl

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/SoftwareApi/authControl?apipost_id=1cd1fd54b84ab3

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用id |
| auth_data | q+u8DdGKcTtETYv2LeFB/tQE0nJbeEZLdNRj1B7zffuJa1x4WJDjtnxSZcVotOPDI8VCwESETE6f5/VNOWhJCPeSjox2TwQq0eIyCNXqa2P4piTW6v+JND31XX13gx3Ut+KCrUQh2Ta5BOY52egBtIZJJRx5DsWP+ADSwHOckdTERVeU8ugqi3srIOnyyCE9mHnrXlRiq6Xz/HQw7XuZ9otMfCyLq8Nvils3G0+duI5pF76YcMrvWrCoXv3YxYfgf81hwlQ9h8IoOVYAFa69wb2OjiewPYyYq9/7tNADn4k+J+eTn90z45Vw0TkxdApyjLDL2fNFPi4c0VAQj4M3hQ== | string | 是 | 授权信息（授权验证成功后返回的 authData 字段） |
| private_key | MIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQIZI2zostDm6sCAggA MBQGCCqGSIb3DQMHBAhcS0/z6Efx7gSCBMjpuXAFQymb4SWSq+2Y0XUJbbW7hLxm qsQfBhRPjA9RthKtZf486EY3tIRA6TQ2lksDWYrVfMZuxzX4e4ZdRcot+0MEQsXd ygwVdfNLfPgPI5URR8poGqnzhEQWWGsXng9tTFNd5FOM1vN7wAMg1n4M6I2f2fiK gwOIf9ijWrje8S+QEnJBV3axD470oEIuMdVDqqUyyl0OzQ/k5/0jrtAWv+yNgfji 6HVIpY3ruqqJpKlScEF5RJodlm4lTeqfmRS8zs+gWlXb7bWQzyooB8aGUejh2CtJ wJqiawG/wNkiKHm3azY17Ahq+vgOBFUtN0OSr427+oZ6ndbAcaOSPPoQFQhiPP5b Td0nisHsLJhuAzNZgRZTgbV6xckeB8Os7QRC4ml51ZJLUWbfXE47ht4096xUncu+ SVj9j87mynSMVUCzfmx0bvkEicvbzib3g1uDIFwa04BFhEgZrDvxcoAwLqSOAFRg h4GqLZC4Z0RdmNNQihKCwBL5+ACIgwBVJFJoCNCbHCHN2NCvsD/Y+IzIqNOihQJn lxTMN7tIedg71dkM3t5UH235pKzWR3cIAJj4WJrIX8/XjU525dLtRuyeBi1FsmTR NmoXA7RQozu2M5vZiq4gG2DtR/pLVnZG0+4ucLzw6Fg/mZJNT1ET4CPHASXLwFf1 9YCAxAtCQbSzwTo72dLUHfenBkA61H0Ob+QOuzkuc/7W/vYiygdlnnV2CK25YVR3 mxG8gQhJh7U13IH4NOkaKlENL1K+vXyqLmj17qp4pYjMMoxcjSLMEpgKJI/E63fq YfXnMvPN/UygS9qq622fq2ojUyy34DdSu32NwdM18hzsHahwvuoJKmmu0T3YlrO2 SABir/R+xPfpzLgHPDd4aIhUE9+IHf5qPyvi93QvupoIf/gNE5dFSb8X4Fov6A72 kqTYTx9DjFBQJyuWmEtM3L4hBNVj82z4DBvQFfGAoenabiC3ClLI43EnEwchMEy+ NI8qgjykli5Gt8APJPYPEgmF776Bz9CInSpA9UAhZueKfwGths45AoJOW/ERMnQ/ lo8S4X7o8Dc0kptH8vYvPJQMv4PC/j8E7OCPoiqA36sGD29KNu3DHVlKeB9MZcr6 z4hpUDZbQn2123gtRHnpdZk01No1ZBchNk4jTYpOAnYtn7BeHGz1SwJ0Ez2lQy++ XLrQTbHCH6gS364R9r5NZguF5/ksKHwF26n82xgA673VCmqA4WACz//RQa62ufOm tkAD0DAvE5K9jiudKVzGz1/fI93JL4fdPQgBf7fyzZZsKWncG0tc1hQeMVzi8fUd y+VxATEMl62fAxj/dZdHUbR77Sm2djPrkp3/J1YLgOAklEmGrJuvXVr4i2KHUC53 BamFCcSTlpURcCM6EkktCFY8+0pPUK6NFjEXDb2aGipc4RTAZs2MuUPxuyT3vrnb rX2uobLp6a7ZelzCkJYlD/NTPUU6mB73HMi5c36LdC9SyWrF3YZWUFpEjzEUl0lO iNkKzWwNW2TdU1J3lfYiafzvLDv+Q393415sWnLafmj+HtKtpGMoFggYWEyaJ0Kl zgPigsQutM6SU3OCK1C2omkXPAaGtg2vhrGh70iWi9QIYzo+rSOmQeSVkEWH/PNV EqI= | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2OpV6KUKtG31pMtmUG15 35kYYGSPKZJFyahxlzZUJiAeMm1a6fLSQ4Dj0Xn9gdptHCqDW4807+nwkbqy9KB6 k/wWf/Ik047snV33/xPUGa2HKmIMV/7FW7kOW78wBK2Rodla8ZxZX5X7LxyGkB/O VzRkDj6osukUkIj1t8nY1mA6iXS2Krt06iXemHHmfeTn3h5nLxWuO+IP6V6yEpKm /Kzu9Zm2lhXfz+ysmQJwIlOFXjCb+LPDfJEL+LWFwnf77WwIEf7Ea4/Vr55MXGyJ KBIoi63i+wh7FVDnFh2b1w8Y1g3dtlFKbvppspmKLARK8j2dIIxcXzRqJoY+LjiX ewIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| type | 1 | string | 是 | 操作类型  1：加次数 2：减次数 |
| count | 10 | string | 是 | 数量 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "增加次数成功",
    "data": {
        "old_number": "0",
        "new_number": 10,
        "operation_count": "10"
    }
}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Software】获取应用公告

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-08-14 09:48:52

> 更新时间: 2026-01-08 14:42:52

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/notice

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/SoftwareApi/notice?apipost_id=1db8a04f784ff8

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| appid | 1 | string | 是 | 应用id |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"code":"1","msg":"获取成功","data":[{"id":1,"title":"AWWWsss","content":"<p>WWFFsss<\/p>","username":"admin","appid":1,"time":"2025-08-14 09:44:20","state":"1","app_name":"Nathan软件"}]}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Software】获取应用版本信息

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-08-14 14:30:07

> 更新时间: 2026-01-08 14:42:52

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/versionData

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/SoftwareApi/versionData?apipost_id=1df9039178410c

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| appid | 1 | string | 是 | 应用id |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"code":"1","msg":"获取成功","data":{"id":1,"app_name":"Nathan软件","app_author":"12","app_url":"12","app_content":"11111<br>3","app_version":"1.0.0","app_update":null,"app_zip":null}}
```

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Software】更新授权验证标识与卡密

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2025-07-02 17:24:06

> 更新时间: 2026-01-08 14:42:52

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/updateAuth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/SoftwareApi/updateAuth?apipost_id=26c3dcdd715b5b

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用id |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI2+aAeZr6m6gCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECApCjRxQCSG5BIIEyLG+NXYFpmuz 0RUoR6jBeRpbBrZbAca/0ztJtZ3ntYDYnkntZIkWlJ4N1+K5V3HJKhj8H2Y1PKM/ 7OOslIA5GpEx54D3c64dqQ2nXeqzxNcHJ/9SVkAcIJalSItRvD7pe1XPjUnRLFAF D7OUVhBF9GPumeKZ1jmenXZYoCKBxOzmso4ZXYlhcJa4cHh1E0xcQRZB8sUoYxhS TVL3/2uTeo6s9JPZWuU0r7IC94A/mDgsW51GLklm2xmG1LXiesNdOC1oPbRti3rE 9Po7D6giEIBwoOw9AlbKLNTgMbq5AEjfzI2Yp68hGxDrIKKe9t+j7Ui7/uUH0Gvt TNCxKqZPkwyr1cZmlXTYQYZkynY/dxi7DVgIiRtlrN5+bgPBpzM8JpFGp4eGgfXW rVuH3CyOkQpCkGHx1ofHPfcPVI4tAwt9qUXaqktyDKM1IXLJw1kLJwCCxj21yK/w o/BCZWtW2vwfVuAi3q9LeAismZNoWtFpXxzkxqe+mMlxzviKRI+0XFCfqGAsAYkx 78cOmbJJTpjnXXoDB5zPcMSyWhEwP99x6QACE5BtX98dq6ykBmUhjfrnx+9McOJH KBUqLE1Q7ZVbgzYRxvg2jkpG3LnEXmT2B07Cnfy5lZqyqprPUW4CKy/e5gNFX4My t9KCH+OQEUjxxKlYu/Lmhht8mSB9PkWfgAwRxdPtePivwAINJBnlrcQwj9jFtWUO e82AMhQZVinoytHEz04dQnJGdt0JguTwx2SS0ifP+/NzWxd51LcxOxluAmlGysDk 17N56I43bHGwq7vjgvIsf4GG1yoAR04sN4SGJbbxzTBL7ZoKbDcuqiDX9xE69InE WIWWzr+oIg8BV5jZI9pYTQubgIruofcYiVdPkyFurXCPxQa5G3Z2kqEz8Rh+aHQY PhrCeXFwS6Ht6o/nIiWTmh/c4uTaCoYKFol0HhVTSiwN58RuXSSV5F6lNwYW/t0S L9WeOQYBoggPi5kPvuYqVtutOhzpbrKkFOYOqTOh42sRscw3XbtkGkaXCy3g1TMI nJxNqhqad5V/A5qUW5giCnpBoMOMTGJQBwl0z7TISUU2F5xkgfwDwnjRKri8WdYv Xo8YpJrTv+c/YScQNW3eOa2+WnqBqIMeEmH93aDc0fMymYOeZddtz1b91DMOme9C mE8Azxnhjrq/tDlqJVCwsmgS+sEhXy0jnPvMsAImYu7l3fJbHp/O8j3Z7pfXq0D+ uJBjZ/sTq0zf73SBIDrjs5sKK4rlp6Ei5+9W7ptveUP1Bhs15SLQKl02l6p058oL xpb13ggZY+CILDLau0t6X9KIoQQrNRnIgZXI75NdIdPjncsIv4QWd63vYLgu2m7i vhYXQJ/Iv9SsCsw82xEZ14ogWNQAp1kOVkDPV0lJNHkAupdFXtXCrDgTArAUMp3F uGs8omhmQLOQy55XZFXabAzv49eAcBU9wl/PkvEYQygVJG0aEoPbAv/q7aqGEcMz l4O2/PlzoRyyownuicvkutNFpp63qhAtujr7cUy4LyH2oQGi9IbIFRKvG8BZfH72 3GpvST87ebST2wW9Jt8twZGo2vFxYCcCKz0xL+FCfFQF6nCHxkTaPqGLQiFSWF6e R/Kd9QGPL63xXtQsdiGYRw== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3cNO98FG7wGfOvvoAAOV OYTrMPCh2eAppHkWXLd0JFzw3Mm/2a8L+jxRozWu2Wj+mpEFhg23CYTNVjA1+1Is pid8x6xT1JQoKi+Sfchh9bt3bz2uYCjyZ76zb91/XmLHgP6+QNXUCHEDot1WbdkS DR1nSBqmW1mflKBhTB+6GvK2+nVTpQHzGodrD23VLGc1skozrnMc78CMCMJ8XuUt NHVNv002gpSNg6LR53lmkY+qyw+k5EpcOeG9NT4GefDElVogYwEICcW99j5KxFD1 cMJ7VELx0yb0udYN0MrEkWBB9S0K2ZV4BKY75G2ZSv+lmxfbxJBoWEKsNMjQ3MO8 twIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| auth_data | O5Wzl06iF2XhDdcL8i4brstvRM4XxCDLdbtmROYl7XPZCsJg8tAgWyjI+cs9YWD6IPDe2BR5aHz5Z4FvnFzFbjDifgfAHlcmr9+1+thUbu3ocxSlnj4X9nzDSezP6k2gpCkLfNR0ll8jYgaXcxf6g5gcKVSAoeeHJnKsSN6SOQePdfBNh0toNXUiJw03UHjtFM4+qcxSr2YjZ8FTXvoXUXeuk4tuGz\/9PxL5Ahg38eXmgvxHK\/bfhGRAHzK5CBSp9qbrRM7PR0AjVo1rczyzHE00\/Nt0HMVWu7NG06wn03eqCOrC4GjOI+FRZtsyCFAP5N3jN6ZG2uP\/JlCbOIlrmQ== | string | 是 | 授权信息（授权验证成功后返回的 authData 字段） |
| verify_data | Nathan | string | 是 | 验证标识 更新此字段则传，不更新勿传 |
| key | NN_jFUI-FoJL-RspG-PJoW | string | 是 | 卡密 更新此字段则传，不更新勿传 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "扣除天数成功",
    "data": {
        "new_authdate": 1727680320
    }
}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Software】授权验证

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-25 15:12:37

> 更新时间: 2026-03-02 17:45:24

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/checkSoftware

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用id |
| verify_data | Nathan | string | 否 | 验证标识 |
| key | 9iIA-uwbj-3vxN-GYWc | string | 否 | 卡密 |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI2+aAeZr6m6gCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECApCjRxQCSG5BIIEyLG+NXYFpmuz 0RUoR6jBeRpbBrZbAca/0ztJtZ3ntYDYnkntZIkWlJ4N1+K5V3HJKhj8H2Y1PKM/ 7OOslIA5GpEx54D3c64dqQ2nXeqzxNcHJ/9SVkAcIJalSItRvD7pe1XPjUnRLFAF D7OUVhBF9GPumeKZ1jmenXZYoCKBxOzmso4ZXYlhcJa4cHh1E0xcQRZB8sUoYxhS TVL3/2uTeo6s9JPZWuU0r7IC94A/mDgsW51GLklm2xmG1LXiesNdOC1oPbRti3rE 9Po7D6giEIBwoOw9AlbKLNTgMbq5AEjfzI2Yp68hGxDrIKKe9t+j7Ui7/uUH0Gvt TNCxKqZPkwyr1cZmlXTYQYZkynY/dxi7DVgIiRtlrN5+bgPBpzM8JpFGp4eGgfXW rVuH3CyOkQpCkGHx1ofHPfcPVI4tAwt9qUXaqktyDKM1IXLJw1kLJwCCxj21yK/w o/BCZWtW2vwfVuAi3q9LeAismZNoWtFpXxzkxqe+mMlxzviKRI+0XFCfqGAsAYkx 78cOmbJJTpjnXXoDB5zPcMSyWhEwP99x6QACE5BtX98dq6ykBmUhjfrnx+9McOJH KBUqLE1Q7ZVbgzYRxvg2jkpG3LnEXmT2B07Cnfy5lZqyqprPUW4CKy/e5gNFX4My t9KCH+OQEUjxxKlYu/Lmhht8mSB9PkWfgAwRxdPtePivwAINJBnlrcQwj9jFtWUO e82AMhQZVinoytHEz04dQnJGdt0JguTwx2SS0ifP+/NzWxd51LcxOxluAmlGysDk 17N56I43bHGwq7vjgvIsf4GG1yoAR04sN4SGJbbxzTBL7ZoKbDcuqiDX9xE69InE WIWWzr+oIg8BV5jZI9pYTQubgIruofcYiVdPkyFurXCPxQa5G3Z2kqEz8Rh+aHQY PhrCeXFwS6Ht6o/nIiWTmh/c4uTaCoYKFol0HhVTSiwN58RuXSSV5F6lNwYW/t0S L9WeOQYBoggPi5kPvuYqVtutOhzpbrKkFOYOqTOh42sRscw3XbtkGkaXCy3g1TMI nJxNqhqad5V/A5qUW5giCnpBoMOMTGJQBwl0z7TISUU2F5xkgfwDwnjRKri8WdYv Xo8YpJrTv+c/YScQNW3eOa2+WnqBqIMeEmH93aDc0fMymYOeZddtz1b91DMOme9C mE8Azxnhjrq/tDlqJVCwsmgS+sEhXy0jnPvMsAImYu7l3fJbHp/O8j3Z7pfXq0D+ uJBjZ/sTq0zf73SBIDrjs5sKK4rlp6Ei5+9W7ptveUP1Bhs15SLQKl02l6p058oL xpb13ggZY+CILDLau0t6X9KIoQQrNRnIgZXI75NdIdPjncsIv4QWd63vYLgu2m7i vhYXQJ/Iv9SsCsw82xEZ14ogWNQAp1kOVkDPV0lJNHkAupdFXtXCrDgTArAUMp3F uGs8omhmQLOQy55XZFXabAzv49eAcBU9wl/PkvEYQygVJG0aEoPbAv/q7aqGEcMz l4O2/PlzoRyyownuicvkutNFpp63qhAtujr7cUy4LyH2oQGi9IbIFRKvG8BZfH72 3GpvST87ebST2wW9Jt8twZGo2vFxYCcCKz0xL+FCfFQF6nCHxkTaPqGLQiFSWF6e R/Kd9QGPL63xXtQsdiGYRw== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3cNO98FG7wGfOvvoAAOV OYTrMPCh2eAppHkWXLd0JFzw3Mm/2a8L+jxRozWu2Wj+mpEFhg23CYTNVjA1+1Is pid8x6xT1JQoKi+Sfchh9bt3bz2uYCjyZ76zb91/XmLHgP6+QNXUCHEDot1WbdkS DR1nSBqmW1mflKBhTB+6GvK2+nVTpQHzGodrD23VLGc1skozrnMc78CMCMJ8XuUt NHVNv002gpSNg6LR53lmkY+qyw+k5EpcOeG9NT4GefDElVogYwEICcW99j5KxFD1 cMJ7VELx0yb0udYN0MrEkWBB9S0K2ZV4BKY75G2ZSv+lmxfbxJBoWEKsNMjQ3MO8 twIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"验证成功","signature":"Bt7YxzNLuwh+k2emDvq9L11q4JwfDEG6qCR87dnTLZli60QJcBEIu12fmRvVYjQ+UtqynoOwjbEjV05zGwa26jVQRV\/N+mF1GROh39wOFhSDovF\/SY+MtlcVedJWbra3Dgg20hAq+9fJFSbuvsfpvvzu6dBPmdxSkEzRcUTUEhUnM2sxOB7dgTOHmqT8mXUUkXDblDLA2vkF+K29L1ZyrvJ4GXlhHAIKQH0ga1Gxqv59C4tbjdbQpDpweH3cv4wgZi1Bmx0PMUTfGfyE6JrVxqFXCf2VZ2LvDHaMCIHIz7a7WyNacdYkH7QMtkMkYQe5M1iOGvMwnWTqklgbIQqsQw==","authData":"q\/9p7fa66O5Wy5MjFEgdBVGJiQWb1YIjdc3zQEri\/WrNlwj0BotxyGbmFEnW27glv9MDKCgVf108Y+sHCAbLZRGGqVNhKAtWCtKEhYzm4aINvNMOR+J97jGcjcuU0dlBEkg5Dj\/vmh1anu3gPTKaL6q3FAnSM3DM\/\/\/9ICRyGiHLTfPbW69zhthpLWDrcnsq1\/C3M+Vk01DH2ok5vE2tA4ETRtdEq59rja\/2BsXJYddZkNIXdIFYrmLqfyPZ+nJhaNXiLXXeZtu4xpOiq5HBU4X2V2pSZ\/Jt17965ICE\/oYbcUdYJ4525SsWP0\/Tgqq7cyI5fK4EM8O5AGx1LCXhcQ==","appParams":"DczlO\/4url4+vrc2CA5aDh6DWFJwtJFbmao5VHhQzQV\/cmyvVz26aT\/V0mhj7woHYGDYFGSiYP3cj1+pr3Mg\/sbFcIQICBvL9C\/Pnqo8gGWNxfHFHHt9fK24MuTFj4D\/2JhYm3zlrH9zRieTGXTEXad8eRzF4CJW9NROpNIFMZAC3Zn5xllRx5o0b8skeunUDkEhrjLPu2o8DigQ3k90fRMkYCxNFsexfikOtl+5ym2adnBZqmv4Krj3WZdF9tkEkjEZUVb0YiDDJb336\/KAnEYnPAwS560j8dlEQsQEsUklHOfxCHrA40DLzStA6Ka9Ky\/3leuK4ZCUxu1yuGu7ZQ=="}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 验证成功 | string | 返回文字描述 |
| signature | Bt7YxzNLuwh+k2emDvq9L11q4JwfDEG6qCR87dnTLZli60QJcBEIu12fmRvVYjQ+UtqynoOwjbEjV05zGwa26jVQRV/N+mF1GROh39wOFhSDovF/SY+MtlcVedJWbra3Dgg20hAq+9fJFSbuvsfpvvzu6dBPmdxSkEzRcUTUEhUnM2sxOB7dgTOHmqT8mXUUkXDblDLA2vkF+K29L1ZyrvJ4GXlhHAIKQH0ga1Gxqv59C4tbjdbQpDpweH3cv4wgZi1Bmx0PMUTfGfyE6JrVxqFXCf2VZ2LvDHaMCIHIz7a7WyNacdYkH7QMtkMkYQe5M1iOGvMwnWTqklgbIQqsQw== | string | 已签名内容（授权验证成功后返回的 signature 字段） |
| authData | q/9p7fa66O5Wy5MjFEgdBVGJiQWb1YIjdc3zQEri/WrNlwj0BotxyGbmFEnW27glv9MDKCgVf108Y+sHCAbLZRGGqVNhKAtWCtKEhYzm4aINvNMOR+J97jGcjcuU0dlBEkg5Dj/vmh1anu3gPTKaL6q3FAnSM3DM///9ICRyGiHLTfPbW69zhthpLWDrcnsq1/C3M+Vk01DH2ok5vE2tA4ETRtdEq59rja/2BsXJYddZkNIXdIFYrmLqfyPZ+nJhaNXiLXXeZtu4xpOiq5HBU4X2V2pSZ/Jt17965ICE/oYbcUdYJ4525SsWP0/Tgqq7cyI5fK4EM8O5AGx1LCXhcQ== | string | 授权信息（获取请用解密接口） |
| appParams | DczlO/4url4+vrc2CA5aDh6DWFJwtJFbmao5VHhQzQV/cmyvVz26aT/V0mhj7woHYGDYFGSiYP3cj1+pr3Mg/sbFcIQICBvL9C/Pnqo8gGWNxfHFHHt9fK24MuTFj4D/2JhYm3zlrH9zRieTGXTEXad8eRzF4CJW9NROpNIFMZAC3Zn5xllRx5o0b8skeunUDkEhrjLPu2o8DigQ3k90fRMkYCxNFsexfikOtl+5ym2adnBZqmv4Krj3WZdF9tkEkjEZUVb0YiDDJb336/KAnEYnPAwS560j8dlEQsQEsUklHOfxCHrA40DLzStA6Ka9Ky/3leuK4ZCUxu1yuGu7ZQ== | string | 应用自定义参数（获取请用解密接口） |

* 失败(404)

```javascript
{"code":"0","msg":"授权已过期"}
```

**Query**

### 【Software】验证签名

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-25 15:08:27

> 更新时间: 2026-01-08 14:42:52

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/verifySign

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 3 | string | 是 | 应用id |
| verify_data | Nathan | string | 否 | 验证标识 |
| key | NN_jFUI-FoJL-RspG-PJoW | string | 否 | 卡密 |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQIIVYRHTMlHY8CAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECEVaysJu2eMABIIEyC7kDWRAUuaU O8cpFB5YqvCMaADLgON0v8kOm0WGZfe9DM+Dgt4FRqo/qo9B4h7f5/jYuvpc+HyJ hzo/Gt7aeJgZfLDjDNnFsZg4MyR1VzATRTzCvOWRCK5f6YQdKp2XH2qdQVURo81D MHMnthTJwGzsnIkU5O+t/DFDwd39RYbbtg8KopL2gMVrApqaCthceGbZ7eehVdUx x7NCrIod6BR/luzR4tKRNw8catQPhSQ2i6mcNHMfZC4A2SD35qMWJJ3N0dDvsLBP KafKRcVGZvh/+O2MhayxoPQYUtTxsFO9Rj3spTnXkTzXlMoNHEcYAen3EbTHBsna ucIjWpwjPSp6bJi0TT/yUE22D+eIUSmvLfEGn/INMgtYKxfVeDtsMesyQFSI8m00 Ib02XyKMR3PYQVvrxkA8N3BFyNiakNKjh7zmjbve5fpGp9Auzs3SMolE4BE14Ofd JfDExuEHxY1tQ0W/fjeD5rRxZtZfafc2clemAICKV7c3nhM/+R4OierxS9jS6icm wu37BYmCFTzX5+cXv3FPWCQxaxuEN5TS4phUhXYgwV2yzCJTkOC1rUfuMiescLgr lQkd5OkXfMy5nfRniaUa578m4TZeyY1ysyc+29YHGsU911KIgdP3Vw/429dpldaY zV07flJ8jSzbfnA228LA3OyAglOaj9b5CVhuQ18M2Bphr3URJ0OFXj3sc9bWcK8K g96yUXxkh20WNhClMo/+VAuOPrE3XrGBhPH960VfHqPsLcLovm7hfSC7kibZRvJ7 TQEmUG37Q4Co31OMp9rIFaqU3v3d2/DlLL2MVF5s4G3IrhGmehU7FX2i+JeARDJl jhx8EVqv8/OBWLOZfR0+q6RSDrrSsbyYyMJFGtjtvcPoq77JDNjQdURi36b1i1rr pxo5IIdZBx1Vtsk23LYkK0i1hwLPimhvVhxyMaytuSDf/aBbqPkr0sJD1Oq23Fyq g/niawKS8cHNyFLnfH823tXQbfJzN4AQ5BnOcq5ii3aMDGAPNXzu2GqzFai3nqCx qkjvyMGhKQefd1k+i3jj3vxOsIllryFm02QQklSTgAzdgAizJ6+h1nvMwDCkytCq qmzny2IGhTz3mShlGX3yko3Ri0+Qg2uIHKoD4/NwEjyGHbI/ql+QF/xSOTbPFwNT cncpNIurETBvOOYOIybzzocq8GVJY4qvGmeBqIlzdydSSzbi4iaZAY3XXtZxOo6A 4nK0dI1pXmFqeu9B/TgW7EpwHKEN/jiqsZIH7mOPnXWDKK6R4kWZzlAfzVF99eWs i6XycrbGmriVK0uzm/50fx6C+FcWshgRSGRBtAWMldRHgS4UA74IaxXjd0mVmd7B Q4UHKXo6opjdOP92HiB71sOG6gJaz2SkMF8Rg16c4X6TMqBzTPsebVecc2B4x43d 8Q7/19LFF2qNrMyvjIgKJDqXK+tvRmrEyFk0pVsewSzqWZv3ilWifOfjrivDTSyd IKgL6uEfekDd7IaEfbREicD01agJolSBjAzK0GiY32kQfWHWqnoht0dgl6mhUd+F tOPMdfnjIYBlU8TS3AKOYuFTFYIS+GRXoy9wv9gadT0YBZCNvhRp8K50rL9X5ctG zepm7Hg9Wx+fSpRTdJAUPg== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA35lCTmRIlanNENmb/Gio P5RmTd4P5CsFLc/yvxB7aDpGsxPh2XArr4rwlT81gaXiB8ZlyPmt8zc9ZS9w92nw an47ld1QcEYu7Mn8LeG/lUZO2IJgS0ej3FsUzPKg/bGgTpwpBrxsNcI+A/xqttg6 KXbiWjwS/nGJJ9b2zwmWPPcqR8flKPi1lHG1eGWfo09Q7KErwD7HPsrCY0B1Ou1K O1eVoiN0bQt4Lor8JVTLInKQ+0Lg9gaVQ/fKeoWyqQ//dMS3s7Wq1HeEUY8cApvI yJcfSlnJgElabNbioM5oPbD8P5P7OGA0yF8tryEnaYouDnPEhoQ19/KHPXeWRr76 bQIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| signature | IwqpKkV4rcf5vLuLkrIvtZJcGPRC4ncDetHOR/agkngjRL9tNrhvl303skpSzKnPvl/OsK5zDjIIM0oDUXOMfaeggTFbGC7CbwFDLmBsMo008qzej+jyuyQwLXzrDWAX9iHa1Fxg7yjHO/iGSYc+nQyDqPBHQ2J8RePoyXA7Gum/Q/KeWWHjCl/YC6j6DoD/c1L/QZGqIwazGp2YwTFA9br7kkpR8JcOp1UACpIWOD5TaeOczPNufypbdkrjFk7w24yCT6j6hPAcVd5kUdw7bZi4yoT+1a1oihrfKMdIaD48t748FHA7GEBMJO546QFwZGMXxD4Ca75iXKEMrXx+IA== | string | 是 | 已签名内容（授权验证成功后返回的 signature 字段） |
| auth_data | 2VV3SBg5m1pXP0dqvpkWIBqEq+ufO4B5ELUIXNR0mXWe2xP3CTUj8RD057vsQpqYgfDHT3ubw+W91EmGJyYVi2odhWt5yU0OfM/qBNiSH2tF4T//Tmn6RaSpoo0x3w4z8XoDul8LVBg6Pca4uKYF43hb8duesWZo7D2Ru4EivCehTA+ITe8qGYAM+L9kROMK55mgzLQM/Tr++NcTEYBixAyr1bx1TAlX5jW3TCVGxhXtZp7o7P/p9qOybcImJdEb+5xPI6d9li3nT7OrhztUszNzkWZ8VvPng0HjHZ+jFkxMPTAuLACUUrfBG3NkpQvUNDOZM27mB1yeYbKH3XJmcA== | string | 是 | 授权信息（授权验证成功后返回的 authData 字段） |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"签名验证成功","isVerified":true}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 签名验证成功 | string | 返回文字描述 |
| isVerified | true | boolean | true成功 false失败 |

* 失败(404)

```javascript
{
	"code": "0",
	"msg": "签名验证失败，签名与授权信息不匹配",
	"isVerified": false
}
```

**Query**

### 【Software】数据解密

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-26 09:26:53

> 更新时间: 2026-01-08 14:42:52

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/decryptData

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用id |
| private_key | MIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQIZI2zostDm6sCAggA MBQGCCqGSIb3DQMHBAhcS0/z6Efx7gSCBMjpuXAFQymb4SWSq+2Y0XUJbbW7hLxm qsQfBhRPjA9RthKtZf486EY3tIRA6TQ2lksDWYrVfMZuxzX4e4ZdRcot+0MEQsXd ygwVdfNLfPgPI5URR8poGqnzhEQWWGsXng9tTFNd5FOM1vN7wAMg1n4M6I2f2fiK gwOIf9ijWrje8S+QEnJBV3axD470oEIuMdVDqqUyyl0OzQ/k5/0jrtAWv+yNgfji 6HVIpY3ruqqJpKlScEF5RJodlm4lTeqfmRS8zs+gWlXb7bWQzyooB8aGUejh2CtJ wJqiawG/wNkiKHm3azY17Ahq+vgOBFUtN0OSr427+oZ6ndbAcaOSPPoQFQhiPP5b Td0nisHsLJhuAzNZgRZTgbV6xckeB8Os7QRC4ml51ZJLUWbfXE47ht4096xUncu+ SVj9j87mynSMVUCzfmx0bvkEicvbzib3g1uDIFwa04BFhEgZrDvxcoAwLqSOAFRg h4GqLZC4Z0RdmNNQihKCwBL5+ACIgwBVJFJoCNCbHCHN2NCvsD/Y+IzIqNOihQJn lxTMN7tIedg71dkM3t5UH235pKzWR3cIAJj4WJrIX8/XjU525dLtRuyeBi1FsmTR NmoXA7RQozu2M5vZiq4gG2DtR/pLVnZG0+4ucLzw6Fg/mZJNT1ET4CPHASXLwFf1 9YCAxAtCQbSzwTo72dLUHfenBkA61H0Ob+QOuzkuc/7W/vYiygdlnnV2CK25YVR3 mxG8gQhJh7U13IH4NOkaKlENL1K+vXyqLmj17qp4pYjMMoxcjSLMEpgKJI/E63fq YfXnMvPN/UygS9qq622fq2ojUyy34DdSu32NwdM18hzsHahwvuoJKmmu0T3YlrO2 SABir/R+xPfpzLgHPDd4aIhUE9+IHf5qPyvi93QvupoIf/gNE5dFSb8X4Fov6A72 kqTYTx9DjFBQJyuWmEtM3L4hBNVj82z4DBvQFfGAoenabiC3ClLI43EnEwchMEy+ NI8qgjykli5Gt8APJPYPEgmF776Bz9CInSpA9UAhZueKfwGths45AoJOW/ERMnQ/ lo8S4X7o8Dc0kptH8vYvPJQMv4PC/j8E7OCPoiqA36sGD29KNu3DHVlKeB9MZcr6 z4hpUDZbQn2123gtRHnpdZk01No1ZBchNk4jTYpOAnYtn7BeHGz1SwJ0Ez2lQy++ XLrQTbHCH6gS364R9r5NZguF5/ksKHwF26n82xgA673VCmqA4WACz//RQa62ufOm tkAD0DAvE5K9jiudKVzGz1/fI93JL4fdPQgBf7fyzZZsKWncG0tc1hQeMVzi8fUd y+VxATEMl62fAxj/dZdHUbR77Sm2djPrkp3/J1YLgOAklEmGrJuvXVr4i2KHUC53 BamFCcSTlpURcCM6EkktCFY8+0pPUK6NFjEXDb2aGipc4RTAZs2MuUPxuyT3vrnb rX2uobLp6a7ZelzCkJYlD/NTPUU6mB73HMi5c36LdC9SyWrF3YZWUFpEjzEUl0lO iNkKzWwNW2TdU1J3lfYiafzvLDv+Q393415sWnLafmj+HtKtpGMoFggYWEyaJ0Kl zgPigsQutM6SU3OCK1C2omkXPAaGtg2vhrGh70iWi9QIYzo+rSOmQeSVkEWH/PNV EqI= | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2OpV6KUKtG31pMtmUG15 35kYYGSPKZJFyahxlzZUJiAeMm1a6fLSQ4Dj0Xn9gdptHCqDW4807+nwkbqy9KB6 k/wWf/Ik047snV33/xPUGa2HKmIMV/7FW7kOW78wBK2Rodla8ZxZX5X7LxyGkB/O VzRkDj6osukUkIj1t8nY1mA6iXS2Krt06iXemHHmfeTn3h5nLxWuO+IP6V6yEpKm /Kzu9Zm2lhXfz+ysmQJwIlOFXjCb+LPDfJEL+LWFwnf77WwIEf7Ea4/Vr55MXGyJ KBIoi63i+wh7FVDnFh2b1w8Y1g3dtlFKbvppspmKLARK8j2dIIxcXzRqJoY+LjiX ewIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| decrypt_data | q+u8DdGKcTtETYv2LeFB/tQE0nJbeEZLdNRj1B7zffuJa1x4WJDjtnxSZcVotOPDI8VCwESETE6f5/VNOWhJCPeSjox2TwQq0eIyCNXqa2P4piTW6v+JND31XX13gx3Ut+KCrUQh2Ta5BOY52egBtIZJJRx5DsWP+ADSwHOckdTERVeU8ugqi3srIOnyyCE9mHnrXlRiq6Xz/HQw7XuZ9otMfCyLq8Nvils3G0+duI5pF76YcMrvWrCoXv3YxYfgf81hwlQ9h8IoOVYAFa69wb2OjiewPYyYq9/7tNADn4k+J+eTn90z45Vw0TkxdApyjLDL2fNFPi4c0VAQj4M3hQ== | string | 是 | 需解密的内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"解密成功","decryptedData":{"id":84,"key":"9iIA-uwbj-3vxN-GYWc","verify_data":"Nathan","contact":"1","appid":1,"appname":"11","authdate":"0","reason":null,"state":1,"number":"-1"}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 解密成功 | string | 返回文字描述 |
| decryptedData | - | object | 解密结果 |
| decryptedData.id | 51 | number | - |
| decryptedData.key | NN_jFUI-FoJL-RspG-PJoW | string | 卡密 |
| decryptedData.verify_data | Nathan | string | 验证标识 |
| decryptedData.contact | 123456 | string | - |
| decryptedData.appid | 3 | number | 应用id |
| decryptedData.appname | 软件 | string | - |
| decryptedData.authdate | 0 | string | 到期时间戳（0为永久） |
| decryptedData.reason | - | null | - |
| decryptedData.state | 1 | number | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Software】扣除授权天数

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-26 10:17:12

> 更新时间: 2026-01-08 14:42:52

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/deductionDays

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用id |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI2+aAeZr6m6gCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECApCjRxQCSG5BIIEyLG+NXYFpmuz 0RUoR6jBeRpbBrZbAca/0ztJtZ3ntYDYnkntZIkWlJ4N1+K5V3HJKhj8H2Y1PKM/ 7OOslIA5GpEx54D3c64dqQ2nXeqzxNcHJ/9SVkAcIJalSItRvD7pe1XPjUnRLFAF D7OUVhBF9GPumeKZ1jmenXZYoCKBxOzmso4ZXYlhcJa4cHh1E0xcQRZB8sUoYxhS TVL3/2uTeo6s9JPZWuU0r7IC94A/mDgsW51GLklm2xmG1LXiesNdOC1oPbRti3rE 9Po7D6giEIBwoOw9AlbKLNTgMbq5AEjfzI2Yp68hGxDrIKKe9t+j7Ui7/uUH0Gvt TNCxKqZPkwyr1cZmlXTYQYZkynY/dxi7DVgIiRtlrN5+bgPBpzM8JpFGp4eGgfXW rVuH3CyOkQpCkGHx1ofHPfcPVI4tAwt9qUXaqktyDKM1IXLJw1kLJwCCxj21yK/w o/BCZWtW2vwfVuAi3q9LeAismZNoWtFpXxzkxqe+mMlxzviKRI+0XFCfqGAsAYkx 78cOmbJJTpjnXXoDB5zPcMSyWhEwP99x6QACE5BtX98dq6ykBmUhjfrnx+9McOJH KBUqLE1Q7ZVbgzYRxvg2jkpG3LnEXmT2B07Cnfy5lZqyqprPUW4CKy/e5gNFX4My t9KCH+OQEUjxxKlYu/Lmhht8mSB9PkWfgAwRxdPtePivwAINJBnlrcQwj9jFtWUO e82AMhQZVinoytHEz04dQnJGdt0JguTwx2SS0ifP+/NzWxd51LcxOxluAmlGysDk 17N56I43bHGwq7vjgvIsf4GG1yoAR04sN4SGJbbxzTBL7ZoKbDcuqiDX9xE69InE WIWWzr+oIg8BV5jZI9pYTQubgIruofcYiVdPkyFurXCPxQa5G3Z2kqEz8Rh+aHQY PhrCeXFwS6Ht6o/nIiWTmh/c4uTaCoYKFol0HhVTSiwN58RuXSSV5F6lNwYW/t0S L9WeOQYBoggPi5kPvuYqVtutOhzpbrKkFOYOqTOh42sRscw3XbtkGkaXCy3g1TMI nJxNqhqad5V/A5qUW5giCnpBoMOMTGJQBwl0z7TISUU2F5xkgfwDwnjRKri8WdYv Xo8YpJrTv+c/YScQNW3eOa2+WnqBqIMeEmH93aDc0fMymYOeZddtz1b91DMOme9C mE8Azxnhjrq/tDlqJVCwsmgS+sEhXy0jnPvMsAImYu7l3fJbHp/O8j3Z7pfXq0D+ uJBjZ/sTq0zf73SBIDrjs5sKK4rlp6Ei5+9W7ptveUP1Bhs15SLQKl02l6p058oL xpb13ggZY+CILDLau0t6X9KIoQQrNRnIgZXI75NdIdPjncsIv4QWd63vYLgu2m7i vhYXQJ/Iv9SsCsw82xEZ14ogWNQAp1kOVkDPV0lJNHkAupdFXtXCrDgTArAUMp3F uGs8omhmQLOQy55XZFXabAzv49eAcBU9wl/PkvEYQygVJG0aEoPbAv/q7aqGEcMz l4O2/PlzoRyyownuicvkutNFpp63qhAtujr7cUy4LyH2oQGi9IbIFRKvG8BZfH72 3GpvST87ebST2wW9Jt8twZGo2vFxYCcCKz0xL+FCfFQF6nCHxkTaPqGLQiFSWF6e R/Kd9QGPL63xXtQsdiGYRw== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3cNO98FG7wGfOvvoAAOV OYTrMPCh2eAppHkWXLd0JFzw3Mm/2a8L+jxRozWu2Wj+mpEFhg23CYTNVjA1+1Is pid8x6xT1JQoKi+Sfchh9bt3bz2uYCjyZ76zb91/XmLHgP6+QNXUCHEDot1WbdkS DR1nSBqmW1mflKBhTB+6GvK2+nVTpQHzGodrD23VLGc1skozrnMc78CMCMJ8XuUt NHVNv002gpSNg6LR53lmkY+qyw+k5EpcOeG9NT4GefDElVogYwEICcW99j5KxFD1 cMJ7VELx0yb0udYN0MrEkWBB9S0K2ZV4BKY75G2ZSv+lmxfbxJBoWEKsNMjQ3MO8 twIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| auth_data | O5Wzl06iF2XhDdcL8i4brstvRM4XxCDLdbtmROYl7XPZCsJg8tAgWyjI+cs9YWD6IPDe2BR5aHz5Z4FvnFzFbjDifgfAHlcmr9+1+thUbu3ocxSlnj4X9nzDSezP6k2gpCkLfNR0ll8jYgaXcxf6g5gcKVSAoeeHJnKsSN6SOQePdfBNh0toNXUiJw03UHjtFM4+qcxSr2YjZ8FTXvoXUXeuk4tuGz\/9PxL5Ahg38eXmgvxHK\/bfhGRAHzK5CBSp9qbrRM7PR0AjVo1rczyzHE00\/Nt0HMVWu7NG06wn03eqCOrC4GjOI+FRZtsyCFAP5N3jN6ZG2uP\/JlCbOIlrmQ== | string | 是 | 授权信息（授权验证成功后返回的 authData 字段） |
| day | 1 | string | 是 | 天数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
    "code": "1",
    "msg": "扣除天数成功",
    "data": {
        "new_authdate": 1727680320
    }
}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Software】心跳开始

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-26 10:41:22

> 更新时间: 2026-01-08 14:42:52

**Token为授权检测成功后返回的，详细可见授权检测接口,必看说明：授权检测通过后返回个token，把这个token带到开始的接口里，记录时间，超过后台网站设置的时间范围就为下线 ，如果在这个时间内再次把token传入开始接口里调用就记录新的在线时间 ，需要手动结束的时候再把token带到结束的接口里,请务必在后台网站设置机器人授权API Token与 时间范围,请务必在后台网站设置机器人授权API Token与 时间范围,请务必在后台网站设置机器人授权API Token与 时间范围**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/onlineStart

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| appid | 1 | string | 是 | 应用id |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI2+aAeZr6m6gCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECApCjRxQCSG5BIIEyLG+NXYFpmuz 0RUoR6jBeRpbBrZbAca/0ztJtZ3ntYDYnkntZIkWlJ4N1+K5V3HJKhj8H2Y1PKM/ 7OOslIA5GpEx54D3c64dqQ2nXeqzxNcHJ/9SVkAcIJalSItRvD7pe1XPjUnRLFAF D7OUVhBF9GPumeKZ1jmenXZYoCKBxOzmso4ZXYlhcJa4cHh1E0xcQRZB8sUoYxhS TVL3/2uTeo6s9JPZWuU0r7IC94A/mDgsW51GLklm2xmG1LXiesNdOC1oPbRti3rE 9Po7D6giEIBwoOw9AlbKLNTgMbq5AEjfzI2Yp68hGxDrIKKe9t+j7Ui7/uUH0Gvt TNCxKqZPkwyr1cZmlXTYQYZkynY/dxi7DVgIiRtlrN5+bgPBpzM8JpFGp4eGgfXW rVuH3CyOkQpCkGHx1ofHPfcPVI4tAwt9qUXaqktyDKM1IXLJw1kLJwCCxj21yK/w o/BCZWtW2vwfVuAi3q9LeAismZNoWtFpXxzkxqe+mMlxzviKRI+0XFCfqGAsAYkx 78cOmbJJTpjnXXoDB5zPcMSyWhEwP99x6QACE5BtX98dq6ykBmUhjfrnx+9McOJH KBUqLE1Q7ZVbgzYRxvg2jkpG3LnEXmT2B07Cnfy5lZqyqprPUW4CKy/e5gNFX4My t9KCH+OQEUjxxKlYu/Lmhht8mSB9PkWfgAwRxdPtePivwAINJBnlrcQwj9jFtWUO e82AMhQZVinoytHEz04dQnJGdt0JguTwx2SS0ifP+/NzWxd51LcxOxluAmlGysDk 17N56I43bHGwq7vjgvIsf4GG1yoAR04sN4SGJbbxzTBL7ZoKbDcuqiDX9xE69InE WIWWzr+oIg8BV5jZI9pYTQubgIruofcYiVdPkyFurXCPxQa5G3Z2kqEz8Rh+aHQY PhrCeXFwS6Ht6o/nIiWTmh/c4uTaCoYKFol0HhVTSiwN58RuXSSV5F6lNwYW/t0S L9WeOQYBoggPi5kPvuYqVtutOhzpbrKkFOYOqTOh42sRscw3XbtkGkaXCy3g1TMI nJxNqhqad5V/A5qUW5giCnpBoMOMTGJQBwl0z7TISUU2F5xkgfwDwnjRKri8WdYv Xo8YpJrTv+c/YScQNW3eOa2+WnqBqIMeEmH93aDc0fMymYOeZddtz1b91DMOme9C mE8Azxnhjrq/tDlqJVCwsmgS+sEhXy0jnPvMsAImYu7l3fJbHp/O8j3Z7pfXq0D+ uJBjZ/sTq0zf73SBIDrjs5sKK4rlp6Ei5+9W7ptveUP1Bhs15SLQKl02l6p058oL xpb13ggZY+CILDLau0t6X9KIoQQrNRnIgZXI75NdIdPjncsIv4QWd63vYLgu2m7i vhYXQJ/Iv9SsCsw82xEZ14ogWNQAp1kOVkDPV0lJNHkAupdFXtXCrDgTArAUMp3F uGs8omhmQLOQy55XZFXabAzv49eAcBU9wl/PkvEYQygVJG0aEoPbAv/q7aqGEcMz l4O2/PlzoRyyownuicvkutNFpp63qhAtujr7cUy4LyH2oQGi9IbIFRKvG8BZfH72 3GpvST87ebST2wW9Jt8twZGo2vFxYCcCKz0xL+FCfFQF6nCHxkTaPqGLQiFSWF6e R/Kd9QGPL63xXtQsdiGYRw== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3cNO98FG7wGfOvvoAAOV OYTrMPCh2eAppHkWXLd0JFzw3Mm/2a8L+jxRozWu2Wj+mpEFhg23CYTNVjA1+1Is pid8x6xT1JQoKi+Sfchh9bt3bz2uYCjyZ76zb91/XmLHgP6+QNXUCHEDot1WbdkS DR1nSBqmW1mflKBhTB+6GvK2+nVTpQHzGodrD23VLGc1skozrnMc78CMCMJ8XuUt NHVNv002gpSNg6LR53lmkY+qyw+k5EpcOeG9NT4GefDElVogYwEICcW99j5KxFD1 cMJ7VELx0yb0udYN0MrEkWBB9S0K2ZV4BKY75G2ZSv+lmxfbxJBoWEKsNMjQ3MO8 twIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| auth_data | O5Wzl06iF2XhDdcL8i4brstvRM4XxCDLdbtmROYl7XPZCsJg8tAgWyjI+cs9YWD6IPDe2BR5aHz5Z4FvnFzFbjDifgfAHlcmr9+1+thUbu3ocxSlnj4X9nzDSezP6k2gpCkLfNR0ll8jYgaXcxf6g5gcKVSAoeeHJnKsSN6SOQePdfBNh0toNXUiJw03UHjtFM4+qcxSr2YjZ8FTXvoXUXeuk4tuGz\/9PxL5Ahg38eXmgvxHK\/bfhGRAHzK5CBSp9qbrRM7PR0AjVo1rczyzHE00\/Nt0HMVWu7NG06wn03eqCOrC4GjOI+FRZtsyCFAP5N3jN6ZG2uP\/JlCbOIlrmQ== | string | 是 | 授权信息（授权验证成功后返回的 authData 字段） |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "添加在线状态成功",
    "data": {
        "time": 1714741664
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 添加在线状态成功 | string | - |
| data | - | object | - |
| data.time | 1714741664 | integer | 当前时间戳 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Software】心跳手动结束

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-26 10:41:31

> 更新时间: 2026-01-08 14:42:52

**Token为授权检测成功后返回的，详细可见授权检测接口,请务必在后台网站设置机器人授权API Token,请务必在后台网站设置机器人授权API Token,请务必在后台网站设置机器人授权API Token**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/onlineEnd

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| appid | 1 | string | 是 | 应用id |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI2+aAeZr6m6gCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECApCjRxQCSG5BIIEyLG+NXYFpmuz 0RUoR6jBeRpbBrZbAca/0ztJtZ3ntYDYnkntZIkWlJ4N1+K5V3HJKhj8H2Y1PKM/ 7OOslIA5GpEx54D3c64dqQ2nXeqzxNcHJ/9SVkAcIJalSItRvD7pe1XPjUnRLFAF D7OUVhBF9GPumeKZ1jmenXZYoCKBxOzmso4ZXYlhcJa4cHh1E0xcQRZB8sUoYxhS TVL3/2uTeo6s9JPZWuU0r7IC94A/mDgsW51GLklm2xmG1LXiesNdOC1oPbRti3rE 9Po7D6giEIBwoOw9AlbKLNTgMbq5AEjfzI2Yp68hGxDrIKKe9t+j7Ui7/uUH0Gvt TNCxKqZPkwyr1cZmlXTYQYZkynY/dxi7DVgIiRtlrN5+bgPBpzM8JpFGp4eGgfXW rVuH3CyOkQpCkGHx1ofHPfcPVI4tAwt9qUXaqktyDKM1IXLJw1kLJwCCxj21yK/w o/BCZWtW2vwfVuAi3q9LeAismZNoWtFpXxzkxqe+mMlxzviKRI+0XFCfqGAsAYkx 78cOmbJJTpjnXXoDB5zPcMSyWhEwP99x6QACE5BtX98dq6ykBmUhjfrnx+9McOJH KBUqLE1Q7ZVbgzYRxvg2jkpG3LnEXmT2B07Cnfy5lZqyqprPUW4CKy/e5gNFX4My t9KCH+OQEUjxxKlYu/Lmhht8mSB9PkWfgAwRxdPtePivwAINJBnlrcQwj9jFtWUO e82AMhQZVinoytHEz04dQnJGdt0JguTwx2SS0ifP+/NzWxd51LcxOxluAmlGysDk 17N56I43bHGwq7vjgvIsf4GG1yoAR04sN4SGJbbxzTBL7ZoKbDcuqiDX9xE69InE WIWWzr+oIg8BV5jZI9pYTQubgIruofcYiVdPkyFurXCPxQa5G3Z2kqEz8Rh+aHQY PhrCeXFwS6Ht6o/nIiWTmh/c4uTaCoYKFol0HhVTSiwN58RuXSSV5F6lNwYW/t0S L9WeOQYBoggPi5kPvuYqVtutOhzpbrKkFOYOqTOh42sRscw3XbtkGkaXCy3g1TMI nJxNqhqad5V/A5qUW5giCnpBoMOMTGJQBwl0z7TISUU2F5xkgfwDwnjRKri8WdYv Xo8YpJrTv+c/YScQNW3eOa2+WnqBqIMeEmH93aDc0fMymYOeZddtz1b91DMOme9C mE8Azxnhjrq/tDlqJVCwsmgS+sEhXy0jnPvMsAImYu7l3fJbHp/O8j3Z7pfXq0D+ uJBjZ/sTq0zf73SBIDrjs5sKK4rlp6Ei5+9W7ptveUP1Bhs15SLQKl02l6p058oL xpb13ggZY+CILDLau0t6X9KIoQQrNRnIgZXI75NdIdPjncsIv4QWd63vYLgu2m7i vhYXQJ/Iv9SsCsw82xEZ14ogWNQAp1kOVkDPV0lJNHkAupdFXtXCrDgTArAUMp3F uGs8omhmQLOQy55XZFXabAzv49eAcBU9wl/PkvEYQygVJG0aEoPbAv/q7aqGEcMz l4O2/PlzoRyyownuicvkutNFpp63qhAtujr7cUy4LyH2oQGi9IbIFRKvG8BZfH72 3GpvST87ebST2wW9Jt8twZGo2vFxYCcCKz0xL+FCfFQF6nCHxkTaPqGLQiFSWF6e R/Kd9QGPL63xXtQsdiGYRw== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3cNO98FG7wGfOvvoAAOV OYTrMPCh2eAppHkWXLd0JFzw3Mm/2a8L+jxRozWu2Wj+mpEFhg23CYTNVjA1+1Is pid8x6xT1JQoKi+Sfchh9bt3bz2uYCjyZ76zb91/XmLHgP6+QNXUCHEDot1WbdkS DR1nSBqmW1mflKBhTB+6GvK2+nVTpQHzGodrD23VLGc1skozrnMc78CMCMJ8XuUt NHVNv002gpSNg6LR53lmkY+qyw+k5EpcOeG9NT4GefDElVogYwEICcW99j5KxFD1 cMJ7VELx0yb0udYN0MrEkWBB9S0K2ZV4BKY75G2ZSv+lmxfbxJBoWEKsNMjQ3MO8 twIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| auth_data | O5Wzl06iF2XhDdcL8i4brstvRM4XxCDLdbtmROYl7XPZCsJg8tAgWyjI+cs9YWD6IPDe2BR5aHz5Z4FvnFzFbjDifgfAHlcmr9+1+thUbu3ocxSlnj4X9nzDSezP6k2gpCkLfNR0ll8jYgaXcxf6g5gcKVSAoeeHJnKsSN6SOQePdfBNh0toNXUiJw03UHjtFM4+qcxSr2YjZ8FTXvoXUXeuk4tuGz\/9PxL5Ahg38eXmgvxHK\/bfhGRAHzK5CBSp9qbrRM7PR0AjVo1rczyzHE00\/Nt0HMVWu7NG06wn03eqCOrC4GjOI+FRZtsyCFAP5N3jN6ZG2uP\/JlCbOIlrmQ== | string | 是 | 授权信息（授权验证成功后返回的 authData 字段） |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "强制离线成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 强制离线成功 | string | - |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Software】心跳查询

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-26 10:41:28

> 更新时间: 2026-01-08 14:42:52

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/queryOnline

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| webkey | Nathan_Auth | string | 是 | 网站密钥 |
| appid | 1 | string | 是 | 应用id |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
    "code": "1",
    "msg": "获取成功！",
    "data": {
        "onlineNum": 0,
        "offlineNum": 0,
        "onlineData": [],
        "offlineData": []
    }
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 获取成功！ | string | - |
| data | - | object | - |
| data.onlineNum | 0 | integer | 在线数量 |
| data.offlineNum | 0 | integer | 离线数量 |
| data.onlineData | - | array | 在线授权信息 |
| data.offlineData | - | array | 离线授权信息 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Software】管理员添加授权

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2024-09-26 18:26:45

> 更新时间: 2026-01-08 14:42:52

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/adminAddAuth

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 3 | string | 是 | 应用ID |
| verify_data | Nathan | string | 是 | 验证标识 |
| key | NN_jFUI-FoJL-RspG-PJoW | string | 是 | 卡密 |
| contact | 2322796106 | string | 是 | 联系人信息 |
| authdate | 0 | string | 是 | 授权天数（0为永久，1为1天） |
| adminname | admin | string | 是 | 管理员用户名 |
| password | 123456 | string | 是 | 管理员密码 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"code":"1","msg":"添加授权成功"}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | 1 | string | - |
| msg | 添加授权成功 | string | 返回文字描述 |

* 失败(404)

```javascript
{
    "code": "0",
    "msg": "网站安全密钥错误，无法操作"
}
```

**Query**

### 【Software】上传特征数据

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-02 17:28:23

> 更新时间: 2026-03-25 09:21:00

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/uploadFeatureData

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/SoftwareApi/uploadFeatureData?apipost_id=1f9fbfcc70c67f

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用id |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI2+aAeZr6m6gCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECApCjRxQCSG5BIIEyLG+NXYFpmuz 0RUoR6jBeRpbBrZbAca/0ztJtZ3ntYDYnkntZIkWlJ4N1+K5V3HJKhj8H2Y1PKM/ 7OOslIA5GpEx54D3c64dqQ2nXeqzxNcHJ/9SVkAcIJalSItRvD7pe1XPjUnRLFAF D7OUVhBF9GPumeKZ1jmenXZYoCKBxOzmso4ZXYlhcJa4cHh1E0xcQRZB8sUoYxhS TVL3/2uTeo6s9JPZWuU0r7IC94A/mDgsW51GLklm2xmG1LXiesNdOC1oPbRti3rE 9Po7D6giEIBwoOw9AlbKLNTgMbq5AEjfzI2Yp68hGxDrIKKe9t+j7Ui7/uUH0Gvt TNCxKqZPkwyr1cZmlXTYQYZkynY/dxi7DVgIiRtlrN5+bgPBpzM8JpFGp4eGgfXW rVuH3CyOkQpCkGHx1ofHPfcPVI4tAwt9qUXaqktyDKM1IXLJw1kLJwCCxj21yK/w o/BCZWtW2vwfVuAi3q9LeAismZNoWtFpXxzkxqe+mMlxzviKRI+0XFCfqGAsAYkx 78cOmbJJTpjnXXoDB5zPcMSyWhEwP99x6QACE5BtX98dq6ykBmUhjfrnx+9McOJH KBUqLE1Q7ZVbgzYRxvg2jkpG3LnEXmT2B07Cnfy5lZqyqprPUW4CKy/e5gNFX4My t9KCH+OQEUjxxKlYu/Lmhht8mSB9PkWfgAwRxdPtePivwAINJBnlrcQwj9jFtWUO e82AMhQZVinoytHEz04dQnJGdt0JguTwx2SS0ifP+/NzWxd51LcxOxluAmlGysDk 17N56I43bHGwq7vjgvIsf4GG1yoAR04sN4SGJbbxzTBL7ZoKbDcuqiDX9xE69InE WIWWzr+oIg8BV5jZI9pYTQubgIruofcYiVdPkyFurXCPxQa5G3Z2kqEz8Rh+aHQY PhrCeXFwS6Ht6o/nIiWTmh/c4uTaCoYKFol0HhVTSiwN58RuXSSV5F6lNwYW/t0S L9WeOQYBoggPi5kPvuYqVtutOhzpbrKkFOYOqTOh42sRscw3XbtkGkaXCy3g1TMI nJxNqhqad5V/A5qUW5giCnpBoMOMTGJQBwl0z7TISUU2F5xkgfwDwnjRKri8WdYv Xo8YpJrTv+c/YScQNW3eOa2+WnqBqIMeEmH93aDc0fMymYOeZddtz1b91DMOme9C mE8Azxnhjrq/tDlqJVCwsmgS+sEhXy0jnPvMsAImYu7l3fJbHp/O8j3Z7pfXq0D+ uJBjZ/sTq0zf73SBIDrjs5sKK4rlp6Ei5+9W7ptveUP1Bhs15SLQKl02l6p058oL xpb13ggZY+CILDLau0t6X9KIoQQrNRnIgZXI75NdIdPjncsIv4QWd63vYLgu2m7i vhYXQJ/Iv9SsCsw82xEZ14ogWNQAp1kOVkDPV0lJNHkAupdFXtXCrDgTArAUMp3F uGs8omhmQLOQy55XZFXabAzv49eAcBU9wl/PkvEYQygVJG0aEoPbAv/q7aqGEcMz l4O2/PlzoRyyownuicvkutNFpp63qhAtujr7cUy4LyH2oQGi9IbIFRKvG8BZfH72 3GpvST87ebST2wW9Jt8twZGo2vFxYCcCKz0xL+FCfFQF6nCHxkTaPqGLQiFSWF6e R/Kd9QGPL63xXtQsdiGYRw== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3cNO98FG7wGfOvvoAAOV OYTrMPCh2eAppHkWXLd0JFzw3Mm/2a8L+jxRozWu2Wj+mpEFhg23CYTNVjA1+1Is pid8x6xT1JQoKi+Sfchh9bt3bz2uYCjyZ76zb91/XmLHgP6+QNXUCHEDot1WbdkS DR1nSBqmW1mflKBhTB+6GvK2+nVTpQHzGodrD23VLGc1skozrnMc78CMCMJ8XuUt NHVNv002gpSNg6LR53lmkY+qyw+k5EpcOeG9NT4GefDElVogYwEICcW99j5KxFD1 cMJ7VELx0yb0udYN0MrEkWBB9S0K2ZV4BKY75G2ZSv+lmxfbxJBoWEKsNMjQ3MO8 twIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| auth_data | vDyPYkzOtljkonxIrEDJmcyv8/Y+UIFnaeyTUpDYzXYbQUcIjBR07Ei/53uCGppbC4qtp/7ZmVRd/Gi0JJQfYmmT4vRWPZgTNrfXdFqTF1mqKw36qsVn5+uuNluffVrnt13OqjyIC6malXiyFY/Krh+kSdyyYAUIzZ79dwTnI9PXwXUDLZVU6r6A2Hp8ijMi8qLGIoFjR23Q1cZDRi0ceEFokRwSNEuLSksSGQbx0/lQEFOWnO2rGgTrGVEWKs+WHxw95yNS00egoh7PMV9O08YNSedl2ud+3JdXZLXpI2oy6G3pDeSv4Dr4hDsO3zdoMVSUT21TryCGEAkFha40xw== | string | 是 | 授权信息（授权验证成功后返回的 authData 字段） |
| feature_data | {"key": "Nathan","Auth": "2322796106"} | string | 是 | 特征数据内容 可以接收任意字符串内容，注意是字符串内容，包括：
JSON 字符串：{"key":"value"}
XML 内容：<data><item>value</item></data>
特殊字符：<>&"' 等
普通文本：任意文本内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"上传特征数据成功","data":{"feature_data":"{\"key\": \"Nathan\",\"Auth\": \"2322796106\"}"}}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 【Software】获取特征数据

> 创建人: Nathan

> 更新人: Nathan

> 创建时间: 2026-03-02 17:29:47

> 更新时间: 2026-03-25 09:21:00

**此接口必须为POST
此接口必须为POST
此接口必须为POST
此接口必须为POST**

**接口状态**

> 已完成

**接口URL**

> http(s)://网站域名/api/SoftwareApi/getFeatureData

| 环境  | URL |
| --- | --- |
| 默认环境 | - |

**Mock URL**

> /api/SoftwareApi/getFeatureData?apipost_id=1fa0168af0c6b0

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| appid | 1 | string | 是 | 应用id |
| private_key | MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQI2+aAeZr6m6gCAggA MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECApCjRxQCSG5BIIEyLG+NXYFpmuz 0RUoR6jBeRpbBrZbAca/0ztJtZ3ntYDYnkntZIkWlJ4N1+K5V3HJKhj8H2Y1PKM/ 7OOslIA5GpEx54D3c64dqQ2nXeqzxNcHJ/9SVkAcIJalSItRvD7pe1XPjUnRLFAF D7OUVhBF9GPumeKZ1jmenXZYoCKBxOzmso4ZXYlhcJa4cHh1E0xcQRZB8sUoYxhS TVL3/2uTeo6s9JPZWuU0r7IC94A/mDgsW51GLklm2xmG1LXiesNdOC1oPbRti3rE 9Po7D6giEIBwoOw9AlbKLNTgMbq5AEjfzI2Yp68hGxDrIKKe9t+j7Ui7/uUH0Gvt TNCxKqZPkwyr1cZmlXTYQYZkynY/dxi7DVgIiRtlrN5+bgPBpzM8JpFGp4eGgfXW rVuH3CyOkQpCkGHx1ofHPfcPVI4tAwt9qUXaqktyDKM1IXLJw1kLJwCCxj21yK/w o/BCZWtW2vwfVuAi3q9LeAismZNoWtFpXxzkxqe+mMlxzviKRI+0XFCfqGAsAYkx 78cOmbJJTpjnXXoDB5zPcMSyWhEwP99x6QACE5BtX98dq6ykBmUhjfrnx+9McOJH KBUqLE1Q7ZVbgzYRxvg2jkpG3LnEXmT2B07Cnfy5lZqyqprPUW4CKy/e5gNFX4My t9KCH+OQEUjxxKlYu/Lmhht8mSB9PkWfgAwRxdPtePivwAINJBnlrcQwj9jFtWUO e82AMhQZVinoytHEz04dQnJGdt0JguTwx2SS0ifP+/NzWxd51LcxOxluAmlGysDk 17N56I43bHGwq7vjgvIsf4GG1yoAR04sN4SGJbbxzTBL7ZoKbDcuqiDX9xE69InE WIWWzr+oIg8BV5jZI9pYTQubgIruofcYiVdPkyFurXCPxQa5G3Z2kqEz8Rh+aHQY PhrCeXFwS6Ht6o/nIiWTmh/c4uTaCoYKFol0HhVTSiwN58RuXSSV5F6lNwYW/t0S L9WeOQYBoggPi5kPvuYqVtutOhzpbrKkFOYOqTOh42sRscw3XbtkGkaXCy3g1TMI nJxNqhqad5V/A5qUW5giCnpBoMOMTGJQBwl0z7TISUU2F5xkgfwDwnjRKri8WdYv Xo8YpJrTv+c/YScQNW3eOa2+WnqBqIMeEmH93aDc0fMymYOeZddtz1b91DMOme9C mE8Azxnhjrq/tDlqJVCwsmgS+sEhXy0jnPvMsAImYu7l3fJbHp/O8j3Z7pfXq0D+ uJBjZ/sTq0zf73SBIDrjs5sKK4rlp6Ei5+9W7ptveUP1Bhs15SLQKl02l6p058oL xpb13ggZY+CILDLau0t6X9KIoQQrNRnIgZXI75NdIdPjncsIv4QWd63vYLgu2m7i vhYXQJ/Iv9SsCsw82xEZ14ogWNQAp1kOVkDPV0lJNHkAupdFXtXCrDgTArAUMp3F uGs8omhmQLOQy55XZFXabAzv49eAcBU9wl/PkvEYQygVJG0aEoPbAv/q7aqGEcMz l4O2/PlzoRyyownuicvkutNFpp63qhAtujr7cUy4LyH2oQGi9IbIFRKvG8BZfH72 3GpvST87ebST2wW9Jt8twZGo2vFxYCcCKz0xL+FCfFQF6nCHxkTaPqGLQiFSWF6e R/Kd9QGPL63xXtQsdiGYRw== | string | 是 | 私钥（注意格式 Base64无换行格式） |
| public_key | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3cNO98FG7wGfOvvoAAOV OYTrMPCh2eAppHkWXLd0JFzw3Mm/2a8L+jxRozWu2Wj+mpEFhg23CYTNVjA1+1Is pid8x6xT1JQoKi+Sfchh9bt3bz2uYCjyZ76zb91/XmLHgP6+QNXUCHEDot1WbdkS DR1nSBqmW1mflKBhTB+6GvK2+nVTpQHzGodrD23VLGc1skozrnMc78CMCMJ8XuUt NHVNv002gpSNg6LR53lmkY+qyw+k5EpcOeG9NT4GefDElVogYwEICcW99j5KxFD1 cMJ7VELx0yb0udYN0MrEkWBB9S0K2ZV4BKY75G2ZSv+lmxfbxJBoWEKsNMjQ3MO8 twIDAQAB | string | 是 | 公钥（注意格式 Base64无换行格式） |
| auth_data | vDyPYkzOtljkonxIrEDJmcyv8/Y+UIFnaeyTUpDYzXYbQUcIjBR07Ei/53uCGppbC4qtp/7ZmVRd/Gi0JJQfYmmT4vRWPZgTNrfXdFqTF1mqKw36qsVn5+uuNluffVrnt13OqjyIC6malXiyFY/Krh+kSdyyYAUIzZ79dwTnI9PXwXUDLZVU6r6A2Hp8ijMi8qLGIoFjR23Q1cZDRi0ceEFokRwSNEuLSksSGQbx0/lQEFOWnO2rGgTrGVEWKs+WHxw95yNS00egoh7PMV9O08YNSedl2ud+3JdXZLXpI2oy6G3pDeSv4Dr4hDsO3zdoMVSUT21TryCGEAkFha40xw== | string | 是 | 授权信息（授权验证成功后返回的 authData 字段） |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{"code":"1","msg":"获取特征数据成功","data":{"feature_data":"{\"key\": \"Nathan\",\"Auth\": \"2322796106\"}"}}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

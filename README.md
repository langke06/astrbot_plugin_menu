# AstrBot 菜单插件 (astrbot_plugin_menu)

一个简单的 AstrBot 插件，提供菜单功能，支持查询订单进度。

## 功能特性

- 📋 **菜单显示** - 发送 `/菜单` 显示功能列表
- 📱 **查进度** - 通过手机号查询订单进度
- ❓ **帮助** - 显示使用说明

## 安装方法

### 从 GitHub 安装

1. 打开 AstrBot WebUI
2. 进入「插件管理」→「安装插件」
3. 选择「从链接安装」
4. 输入：`https://github.com/langke06/astrbot_plugin_menu`
5. 点击安装

## 配置说明

安装后，在插件配置中设置：

| 配置项 | 说明 | 示例 |
|--------|------|------|
| `query_url` | 查进度 API 地址 | `http://your-domain.com/api/index.php` |

## 使用方法

### 显示菜单
```
/菜单
```

### 查询订单进度
```
/查进度 19914282289
```

### 显示帮助
```
/help
```

## 查询结果示例

```
📱 手机号：19914282289
📦 共找到 3 个订单
━━━━━━━━━━━━━━━━

【订单 1】
📌 平台：黑色 学习通考试【手动交卷】
🏫 学校：自动识别
📚 课程：形势与政策6测试卷
📊 进度：0%
✅ 状态：已完成
🕐 下单时间：2026-04-24 14:01:51
📝 备注：〖作答记录：41/41；答题完毕，请前往提交〗

...
```

## 文件结构

```
astrbot_plugin_menu/
├── main.py              # 插件主代码
├── metadata.yaml        # 插件元数据
├── requirements.txt     # 依赖
├── _conf_schema.json    # 配置模式
└── README.md           # 本文件
```

## 依赖

- `aiohttp>=3.8.0`
- `pyyaml>=6.0`

## 开发文档

详见 `docs/` 目录：
- `plugin-new.md` - AstrBot 插件开发指南
- `simple.md` - 最小实例

## 作者

- **Author**: langke06
- **Version**: 1.0.8
- **Repository**: https://github.com/langke06/astrbot_plugin_menu

## 许可证

MIT License

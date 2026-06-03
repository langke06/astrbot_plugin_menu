# AstrBot 插件开发指南

## 环境准备

### 获取插件模板

1. 打开 AstrBot 插件模板: [helloworld](https://github.com/Soulter/helloworld)
2. 点击右上角的 `Use this template`
3. 然后点击 `Create new repository`
4. 在 `Repository name` 处填写您的插件名。插件名格式:
   - 推荐以 `astrbot_plugin_` 开头
   - 不能包含空格
   - 保持全部字母小写
   - 尽量简短
5. 点击右下角的 `Create repository`

### 克隆项目到本地

```bash
git clone https://github.com/AstrBotDevs/AstrBot
mkdir -p AstrBot/data/plugins
cd AstrBot/data/plugins
git clone 插件仓库地址
```

然后，使用 `VSCode` 打开 `AstrBot` 项目。找到 `data/plugins/<你的插件名字>` 目录。

更新 `metadata.yaml` 文件，填写插件的元数据信息。

> **WARNING**: 请务必修改此文件，AstrBot 识别插件元数据依赖于 `metadata.yaml` 文件。

### 设置插件 Logo（可选）

可以在插件目录下添加 `logo.png` 文件作为插件的 Logo。请保持长宽比为 1:1，推荐尺寸为 256x256。

### 插件展示名（可选）

可以修改(或添加) `metadata.yaml` 文件中的 `display_name` 字段，作为插件在插件市场等场景中的展示名。

### 插件短描述（可选）

你可以在 `metadata.yaml` 中新增 `short_desc` 字段，作为插件市场卡片上的短描述。

```yaml
short_desc: 一句话介绍你的插件。
```

### 声明支持平台（Optional）

你可以在 `metadata.yaml` 中新增 `support_platforms` 字段（`list[str]`），声明插件支持的平台适配器。

```yaml
support_platforms:
  - telegram
  - discord
```

支持的值：
- `aiocqhttp`
- `qq_official`
- `qq_official_webhook`
- `telegram`
- `wecom`
- `wecom_ai_bot`
- `lark`
- `dingtalk`
- `discord`
- `slack`
- `kook`
- `vocechat`
- `weixin_official_account`
- `weixin_oc`
- `satori`
- `misskey`
- `line`
- `matrix`
- `mattermost`

### 声明 AstrBot 版本范围（Optional）

你可以在 `metadata.yaml` 中新增 `astrbot_version` 字段，声明插件要求的 AstrBot 版本范围。

```yaml
astrbot_version: ">=4.16,<5"
```

可选示例：
- `>=4.17.0`
- `>=4.16,<5`
- `~=4.17`

### 调试插件

AstrBot 采用在运行时注入插件的机制。因此，在调试插件时，需要启动 AstrBot 本体。

您可以使用 AstrBot 的热重载功能简化开发流程。

插件的代码修改后，可以在 AstrBot WebUI 的插件管理处找到自己的插件，点击右上角 `...` 按钮，选择 `重载插件`。

### 插件依赖管理

目前 AstrBot 对插件的依赖管理使用 `pip` 自带的 `requirements.txt` 文件。如果你的插件需要依赖第三方库，请务必在插件目录下创建 `requirements.txt` 文件并写入所使用的依赖库。

## 开发原则

- 功能需经过测试
- 需包含良好的注释
- **持久化数据请存储于 `data` 目录下，而非插件自身目录**，防止更新/重装插件时数据被覆盖
- 良好的错误处理机制，不要让插件因一个错误而崩溃
- 在进行提交前，请使用 [ruff](https://docs.astral.sh/ruff/) 工具格式化您的代码
- **不要使用 `requests` 库来进行网络请求**，可以使用 `aiohttp`, `httpx` 等异步网络请求库
- 如果是对某个插件进行功能扩增，请优先给那个插件提交 PR

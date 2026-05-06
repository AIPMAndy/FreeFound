# 使用指南

## 📖 快速开始

### 1. 查看数据

**在线查看**：访问 [FreeFound 网页版](https://aipmAndy.github.io/FreeFound/)

**本地查看**：
```bash
# 克隆项目
git clone https://github.com/AIPMAndy/FreeFound.git
cd FreeFound

# 查看黑客松数据
cat data/hackathons.json

# 查看孵化器数据
cat data/incubators.json
```

### 2. 运行数据收集器

```bash
# 安装依赖
pip install requests beautifulsoup4

# 运行收集器
python collector.py
```

### 3. 本地预览网页

```bash
# 使用 Python 启动本地服务器
python -m http.server 8000

# 访问 http://localhost:8000
```

## 🔧 高级用法

### 自定义数据收集

编辑 `collector.py`，添加新的数据源：

```python
class HackathonCollector:
    def collect_your_source(self):
        """收集你的数据源"""
        url = "https://your-source.com/api"
        # 实现你的收集逻辑
        pass
```

### 定时自动更新

项目已配置 GitHub Actions，每天自动更新数据。

手动触发更新：
1. 进入 GitHub 仓库
2. 点击 Actions 标签
3. 选择 "自动更新数据" workflow
4. 点击 "Run workflow"

### API 使用

直接访问 JSON 数据：

```bash
# 黑客松数据
curl https://raw.githubusercontent.com/AIPMAndy/FreeFound/main/data/hackathons.json

# 孵化器数据
curl https://raw.githubusercontent.com/AIPMAndy/FreeFound/main/data/incubators.json
```

在你的项目中使用：

```javascript
// JavaScript
fetch('https://raw.githubusercontent.com/AIPMAndy/FreeFound/main/data/hackathons.json')
  .then(response => response.json())
  .then(data => console.log(data));
```

```python
# Python
import requests

url = "https://raw.githubusercontent.com/AIPMAndy/FreeFound/main/data/hackathons.json"
data = requests.get(url).json()
print(data)
```

## 📊 数据格式说明

### 黑客松数据

```json
{
  "title": "活动名称",
  "time": "2026.05.01-2026.05.30",
  "location": "城市/地区",
  "organizer": "主办方",
  "link": "活动链接",
  "source": "数据来源",
  "collected_at": "2026-05-06T20:00:00"
}
```

### 孵化器数据

```json
{
  "name": "孵化器名称",
  "location": "所在城市",
  "address": "详细地址",
  "type": "孵化器类型",
  "focus": "关注领域",
  "website": "官网",
  "contact": "联系方式",
  "services": ["服务1", "服务2"],
  "source": "数据来源"
}
```

## 🤝 贡献数据

### 方式一：提交 Issue

1. 进入 [Issues](https://github.com/AIPMAndy/FreeFound/issues)
2. 点击 "New Issue"
3. 选择 "数据补充" 模板
4. 填写活动或孵化器信息

### 方式二：提交 Pull Request

1. Fork 本项目
2. 编辑 `data/hackathons.json` 或 `data/incubators.json`
3. 提交 Pull Request

**数据质量要求**：
- ✅ 信息准确、来源可靠
- ✅ 包含必要字段（名称、链接、时间/地点）
- ✅ 注明数据来源
- ❌ 不要添加过期活动（超过3个月）
- ❌ 不要添加虚假或广告信息

### 方式三：添加新数据源

如果你发现了好的数据源，欢迎：
1. 在 `collector.py` 中添加新的收集器
2. 提交 Pull Request
3. 在 PR 描述中说明数据源和收集逻辑

## 🔍 搜索和筛选

### 网页版搜索

访问网页版，使用搜索框：
- 按活动名称搜索
- 按城市筛选
- 按主办方查找

### 命令行筛选

```bash
# 筛选北京的黑客松
cat data/hackathons.json | jq '.[] | select(.location | contains("北京"))'

# 筛选2026年的活动
cat data/hackathons.json | jq '.[] | select(.time | contains("2026"))'

# 筛选特定类型的孵化器
cat data/incubators.json | jq '.[] | select(.type == "综合孵化器")'
```

## 📱 订阅更新

### GitHub Watch

1. 点击仓库右上角的 "Watch"
2. 选择 "Custom" → "Releases"
3. 每次数据更新会收到通知

### RSS 订阅

订阅 GitHub Commits RSS：
```
https://github.com/AIPMAndy/FreeFound/commits/main.atom
```

## 🐛 问题反馈

遇到问题？
1. 查看 [FAQ](https://github.com/AIPMAndy/FreeFound/wiki/FAQ)
2. 搜索 [已有 Issues](https://github.com/AIPMAndy/FreeFound/issues)
3. 提交新的 Issue

## 📄 License

MIT License - 自由使用、修改和分发

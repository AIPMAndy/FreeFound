# FreeFound 🚀

**免费找资源 - 黑客松与孵化器信息聚合平台**

> 🎯 **一站式发现全国黑客松活动和创业孵化器** | 自动更新 | 数据开放 | 完全免费

[![GitHub stars](https://img.shields.io/github/stars/AIPMAndy/FreeFound?style=social)](https://github.com/AIPMAndy/FreeFound)
[![GitHub forks](https://img.shields.io/github/forks/AIPMAndy/FreeFound?style=social)](https://github.com/AIPMAndy/FreeFound/fork)
[![GitHub issues](https://img.shields.io/github/issues/AIPMAndy/FreeFound)](https://github.com/AIPMAndy/FreeFound/issues)
[![License](https://img.shields.io/github/license/AIPMAndy/FreeFound)](https://github.com/AIPMAndy/FreeFound/blob/main/LICENSE)

---

## 💡 为什么需要 FreeFound？

**痛点**：
- 🔍 黑客松信息分散在各个平台，找起来太费劲
- 📅 错过了很多优质活动，事后才知道
- 🏢 想找孵化器，但不知道哪些靠谱
- 🌐 需要一个地方能看到全国的创业资源

**解决方案**：
- ✅ 自动聚合全国黑客松活动（50+ 条，覆盖 30+ 城市）
- ✅ 整理优质孵化器信息（31 家，一线城市全覆盖）
- ✅ 每日自动更新，不错过任何机会
- ✅ 数据开放，API 免费使用

---

## ✨ 特性

- 🎯 **黑客松聚合** - 自动收集全国线上/线下黑客松活动
- 🏢 **孵化器名录** - 整理北京及全国创业孵化器信息
- 🤖 **自动更新** - GitHub Actions 每日自动更新数据
- 🌐 **Web 界面** - 美观的网页展示和搜索功能
- 🔌 **REST API** - 提供简单的 API 接口
- 📊 **数据开放** - JSON 格式，易于使用和扩展

## 📊 当前数据

- **黑客松活动**: **50+ 条**（覆盖全国 30+ 城市，2026 年最新）
- **孵化器**: **31 家**（北京、上海、深圳、杭州）
- **数据来源**: 活动行、Devpost、36氪、政府平台、产业园区
- **更新频率**: 每日自动更新（GitHub Actions）

## 🚀 快速开始

### 在线使用

**网页版**：[https://aipmAndy.github.io/FreeFound/](https://aipmAndy.github.io/FreeFound/)

**API 访问**：
```bash
# 获取黑客松列表
curl https://raw.githubusercontent.com/AIPMAndy/FreeFound/main/data/hackathons.json

# 获取孵化器列表
curl https://raw.githubusercontent.com/AIPMAndy/FreeFound/main/data/incubators.json
```

### 本地使用

```bash
# 克隆项目
git clone https://github.com/AIPMAndy/FreeFound.git
cd FreeFound

# 查看数据
cat data/hackathons.json
cat data/incubators.json

# 启动 Web 界面
python -m http.server 8000
# 访问 http://localhost:8000

# 启动 API 服务
python api_server.py 8080
# 访问 http://localhost:8080
```

### 运行数据收集器

```bash
# 安装依赖
pip install requests beautifulsoup4

# 运行收集器
python collector.py
```

## 📁 项目结构

```
FreeFound/
├── data/                      # 数据目录
│   ├── hackathons.json       # 黑客松数据
│   └── incubators.json       # 孵化器数据
├── .github/
│   └── workflows/
│       └── update-data.yml   # 自动更新工作流
├── index.html                # Web 界面
├── collector.py              # 数据收集器
├── api_server.py             # API 服务器
├── README.md                 # 项目说明
├── USAGE.md                  # 使用指南
├── CONTRIBUTING.md           # 贡献指南
└── .gitignore
```

## 📖 使用文档

### 数据格式

**黑客松数据**：
```json
{
  "title": "活动名称",
  "time": "2026.05.01-2026.05.30",
  "location": "城市/地区",
  "organizer": "主办方",
  "link": "活动链接",
  "source": "数据来源"
}
```

**孵化器数据**：
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

### API 接口

启动 API 服务器后，可以使用以下接口：

```bash
# 获取所有黑客松
GET http://localhost:8080/api/hackathons

# 按地点筛选
GET http://localhost:8080/api/hackathons?location=北京

# 按来源筛选
GET http://localhost:8080/api/hackathons?source=活动行

# 限制返回数量
GET http://localhost:8080/api/hackathons?limit=10

# 获取所有孵化器
GET http://localhost:8080/api/incubators

# 按地点筛选
GET http://localhost:8080/api/incubators?location=北京

# 按类型筛选
GET http://localhost:8080/api/incubators?type=综合孵化器

# 获取统计信息
GET http://localhost:8080/api/stats
```

详细文档请查看 [USAGE.md](USAGE.md)

## 🤝 贡献指南

我们欢迎任何形式的贡献！

### 贡献方式

1. **补充数据** - 添加新的黑客松或孵化器信息
2. **改进代码** - 优化收集器、添加新数据源
3. **完善文档** - 改进说明文档、添加使用案例
4. **反馈建议** - 提交 Issue 或参与讨论

### 快速贡献

```bash
# 1. Fork 项目
# 2. 创建分支
git checkout -b feature/your-feature

# 3. 提交更改
git commit -m "feat: 添加新功能"

# 4. 推送分支
git push origin feature/your-feature

# 5. 创建 Pull Request
```

详细指南请查看 [CONTRIBUTING.md](CONTRIBUTING.md)

## 📝 数据来源

- [活动行](https://www.huodongxing.com/) - 国内活动平台
- [Devpost](https://devpost.com/) - 国际黑客松平台
- [SegmentFault](https://segmentfault.com/) - 思否技术社区
- [掘金](https://juejin.cn/) - 技术社区
- [36氪](https://www.36kr.com/) - 创投资讯
- [IT桔子](https://www.itjuzi.com/) - 创投数据库
- 各孵化器官网公开信息

## 🔮 未来计划

- [ ] 自动化爬虫定期更新数据 ✅
- [ ] 添加更多数据源（掘金、CSDN、开源中国等）
- [ ] 开发 Web 界面展示数据 ✅
- [ ] 提供 REST API 接口 ✅
- [ ] AI Agent 自动参与黑客松
- [ ] 邮件/微信订阅新活动通知
- [ ] 孵化器申请条件和成功案例
- [ ] 移动端 App
- [ ] 数据可视化分析
- [ ] 社区论坛和交流

## 📅 更新日志

### v1.0.0 (2026-05-06)

- ✨ 项目初始化
- 📊 收集首批数据（9个黑客松，10家孵化器）
- 🤖 实现自动化数据收集器
- 🌐 开发 Web 展示界面
- 🔌 提供 REST API 接口
- 📚 完善项目文档
- ⚙️ 配置 GitHub Actions 自动更新

## 📄 License

[MIT License](LICENSE)

## 💬 联系方式

- **GitHub Issues**: [提交问题](https://github.com/AIPMAndy/FreeFound/issues)
- **GitHub Discussions**: [参与讨论](https://github.com/AIPMAndy/FreeFound/discussions)
- **Email**: 通过 GitHub Profile 联系维护者

## 🌟 Star History

如果这个项目对你有帮助，请给我们一个 Star ⭐️

[![Star History Chart](https://api.star-history.com/svg?repos=AIPMAndy/FreeFound&type=Date)](https://star-history.com/#AIPMAndy/FreeFound&Date)

## 🙏 致谢

感谢所有贡献者和支持者！

---

**FreeFound** - 让创业资源触手可及 🚀

Made with ❤️ by FreeFound Community

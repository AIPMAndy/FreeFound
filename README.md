# FreeFound

**免费找资源 - 黑客松与孵化器信息聚合平台**

自动收集和聚合全国黑客松活动、创业孵化器、投资资源信息的开源项目。

## 📊 当前数据

- **黑客松活动**: 9+ 条（持续更新）
- **孵化器**: 10+ 家（北京为主）
- **数据来源**: 活动行、Devpost、36氪、公开信息

## 🎯 项目目标

1. **黑客松收集器**
   - 全国线上/线下黑客松活动
   - 自动监控新活动发布
   - 报名信息、奖金、主题整理

2. **孵化器收集器**
   - 北京及全国孵化器名录
   - 投资资源、申请条件
   - 联系方式和服务内容

3. **AI Agent 自动化**（规划中）
   - 自动报名符合条件的黑客松
   - 智能筛选和推荐
   - 自动生成项目提案

## 📁 数据结构

```
data/
├── hackathons.json      # 黑客松活动数据
└── incubators.json      # 孵化器数据
```

### 黑客松数据格式

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

### 孵化器数据格式

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

## 🚀 快速开始

```bash
# 克隆项目
git clone https://github.com/YOUR_USERNAME/FreeFound.git
cd FreeFound

# 查看数据
cat data/hackathons.json
cat data/incubators.json
```

## 📝 数据来源

- [活动行](https://www.huodongxing.com/) - 国内活动平台
- [Devpost](https://devpost.com/) - 国际黑客松平台
- [36氪](https://www.36kr.com/) - 创投资讯
- 各孵化器官网公开信息

## 🤝 贡献指南

欢迎提交 PR 补充更多数据！

1. Fork 本项目
2. 添加新的黑客松或孵化器信息到对应 JSON 文件
3. 提交 Pull Request

### 数据质量要求

- 信息准确、来源可靠
- 包含必要字段（名称、链接、时间/地点）
- 注明数据来源

## 📅 更新日志

- **2026-05-06**: 项目初始化，收集首批数据
  - 9个黑客松活动（活动行）
  - 10家北京孵化器

## 🔮 未来计划

- [ ] 自动化爬虫定期更新数据
- [ ] 添加更多数据源（掘金、CSDN、开源中国等）
- [ ] 开发 Web 界面展示数据
- [ ] AI Agent 自动参与黑客松
- [ ] 邮件/微信订阅新活动通知
- [ ] 孵化器申请条件和成功案例

## 📄 License

MIT License

## 💬 联系方式

- 提交 Issue: [GitHub Issues](https://github.com/YOUR_USERNAME/FreeFound/issues)
- 讨论交流: [GitHub Discussions](https://github.com/YOUR_USERNAME/FreeFound/discussions)

---

**FreeFound** - 让创业资源触手可及 🚀

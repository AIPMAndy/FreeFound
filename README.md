# FreeFound · 先做产品，再谈融资

> 面向大学生、独立开发者和早期创业团队的 **0 → 1 实践指南 + 开源创业资源入口**。

🌐 **网站**：https://aipmandy.github.io/FreeFound/  
📚 **30 天行动指南**：[从问题到真实用户](guides/30-day-startup.md)  
🧪 **对抗式审核**：[审核记录与风险](AUDIT.md)  
👤 **作者**：AI 酋长 Andy · https://metaver.vip/ · 微信 `AIPMAndy`

## 一句话讲清楚

大学生创业，先找真实需求，认识开发者，做出 Demo，找用户验证，再决定要不要融资。黑客松是学习和合作机会，不等于已经找到了市场。

## 核心能力

| 模块 | 用途 | 真实性边界 |
| --- | --- | --- |
| **精选资源入口** | 持续访问 Devpost、MLH、YC 等活动、创业学习和组队平台 | 入口是平台官网，不代表任一活动当前可报名 |
| **黑客松档案** | 保存有来源链接的历史活动，帮助研究过往主题与主办方 | **6 条记录（2 条经官方页面核对的日期未过活动 + 4 条历史记录）**；日期未过不保证正在报名 |
| **孵化机构线索** | 提供区域、类型、服务方向、官网线索 | **31 条待人工核验线索**，不保证正在运营或接收申请 |
| **30 天行动指南** | 问题访谈 → 协作 → Demo → 用户验证 | 方法论示例，不保证融资或商业结果 |
| **本地 API** | `python api_server.py` 后提供 JSON 查询 | GitHub Pages **不提供**托管 API 服务 |

## 数据可信度

2026-10-22 代码审核发现：原始的 50 条黑客松中 **46 条使用 `example.com` 虚构占位网址**，已从公开 JSON 移除。剩余的旧记录 4 条均已过期；另加入 2 条经官方活动页与规则核对的有时限活动，仍需按官网核实报名。对于孵化机构，网站统一显示待核验线索。**数量少一点可以，误导用户报名不行。**

此前文档宣称每天自动更新，但仓库缺少对应自动化流程，因此删除该说法。新增 GitHub Actions 只验证数据结构和阻止占位链接，**不代表活动实时验证**。本项目没有自动验证所有外部网站真实性的能力。

## 快速使用

### 直接打开网站

https://aipmandy.github.io/FreeFound/

### 本地静态网站

```bash
git clone https://github.com/AIPMAndy/FreeFound.git
cd FreeFound
python3 -m http.server 8000
# 浏览器打开 http://localhost:8000
```

### 数据校验

```bash
python3 scripts/validate_data.py
python3 collector.py
```

### 本地 API（不等于线上 API）

```bash
python3 api_server.py 8080
curl "http://localhost:8080/api/hackathons"
curl "http://localhost:8080/api/incubators?location=北京"
```

### 静态数据

- [精选平台与资源入口](data/resources.json)
- [有来源链接的黑客松历史记录](data/hackathons.json)
- [待核验机构资料](data/incubators.json)

## 贡献新活动的最低门槛

请先读 [CONTRIBUTING.md](CONTRIBUTING.md)。具体记录至少包含：真实名称、主办方 / 来源、原始网址、开始结束日期、地区、核验日期与确认方式。严禁 `example.com` 及虚构的“正在报名”状态。未能核实的信息在 Issue 中作为**线索**提交，不得假装真实开放。

## 项目边界

- 这是开放资源目录，不是政府认证名录、投资建议或法律意见。
- 报名资格、截止日期、城市、奖金、孵化器是否继续运营，一律以官方公告为准。
- 硬科技等资本密集领域可能早于收入阶段融资，需要分别评估研发周期与成本。
- **当前网站不会宣称“实时活动”“自动核验”“所有资源已认证”。** 已人工核对的日期只证明核对时资料存在，并不保证后续没有变更。

## 技术结构

```
FreeFound/
├── index.html                  # GitHub Pages 单页站
├── data/
│   ├── resources.json          # 稳定资源入口
│   ├── hackathons.json         # 已有历史活动（移除虚构占位）
│   └── incubators.json         # 待核验机构线索
├── guides/30-day-startup.md    # 0→1 行动指南
├── scripts/validate_data.py    # 离线质量检测
├── .github/workflows/validate.yml # PR/Push 校验
├── collector.py                # 安全只读数据审计
├── api_server.py               # 本地 REST API
├── AUDIT.md                    # 对抗式审核记录
└── LICENSE
```

欢迎在 [Issues](https://github.com/AIPMAndy/FreeFound/issues) 提交官方活动来源、坏链、机构运营情况和勘误。请勿向本仓库提交个人联系方式或未经同意的私人数据。

**作者：AI 酋长 Andy** · [官网](https://metaver.vip/) · [咨询与陪跑](https://metaver.vip/services) · 微信搜索 `AIPMAndy`

MIT License

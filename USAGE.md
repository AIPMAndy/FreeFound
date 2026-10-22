# FreeFound 使用指南

本指南最后校对：2026-10-22。

## 网站与数据

- [GitHub Pages 在线网站](https://aipmandy.github.io/FreeFound/)
- [长期资源入口](data/resources.json)
- [历史黑客松](data/hackathons.json)
- [孵化机构线索](data/incubators.json)
- [30 天创业验证路径](guides/30-day-startup.md)

**数据状态说明：**当前黑客松清单有 2 条截至 2026-10-22 日期尚未结束且核对过官方规则的活动、4 条历史记录；机构资料有 31 条，尚未逐一核验现时运营状态。页面按活动结束日期判定“已结束”，不会自动证明正在报名。请到主办方官网核实参与资格和申请细则。

### 搜索和筛选

1. 在“精选入口 / 黑客松档案 / 孵化机构线索”之间切换。
2. 输入关键词搜索名称、地点、方向或标签。
3. 使用主题筛选。黑客松“仅未结束活动”只代表日期没过，不代表报名仍开放。
4. 点击外部链接时将进入独立第三方站点。

## 本地启动

~~~bash
git clone https://github.com/AIPMAndy/FreeFound.git
cd FreeFound
python3 -m http.server 8000
~~~

浏览器访问 http://localhost:8000 ，**不要双击 HTML 直接以 file:// 打开**，否则浏览器可能阻止 JSON fetch。

## 本地 API

网站是静态 GitHub Pages；`api_server.py` **不是在线托管 API**，需要用户在自己电脑上运行。

~~~bash
python3 api_server.py 8080
curl "http://localhost:8080/api/hackathons"
curl "http://localhost:8080/api/incubators?location=北京"
curl "http://localhost:8080/api/stats"
~~~

接口：

| 路径 | 可选参数 |
| --- | --- |
| /api/hackathons | location, source, q, limit |
| /api/incubators | location, type, q, limit |
| /api/resources | category, q, limit |
| /api/stats | 无 |

`limit` 必须是 1–200 之间的整数；默认 100。JSON 返回的活动历史不等于实时报名信息。

## 数据贡献

请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。直接提交已核实的活动时，需要原始主办方来源、起止日期、地区、核验时间和证据链接。仅有微信群截图或无来源文字，先提交 Issue 作为**待核验线索**，不要并入活动清单。

## 数据检测

~~~bash
python3 scripts/validate_data.py
python3 -m unittest discover -s tests -v
~~~

CI 阻止明显无效链接、坏日期和重复内容；**CI 通过不意味着真人已验证活动真实、机构在营业或报名开放**。

联系作者：[metaver.vip](https://metaver.vip/) · 微信 `AIPMAndy`。

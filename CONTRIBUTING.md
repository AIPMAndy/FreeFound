# 贡献指南

感谢你对 FreeFound 项目的关注！我们欢迎任何形式的贡献。

## 🎯 贡献方式

### 1. 补充数据

**最简单的贡献方式**：补充黑客松或孵化器信息

- 提交 Issue 告诉我们
- 或直接编辑 JSON 文件提交 PR

### 2. 改进代码

- 优化数据收集器
- 添加新的数据源
- 改进网页界面
- 修复 Bug

### 3. 完善文档

- 改进 README
- 补充使用案例
- 翻译文档

### 4. 分享传播

- Star 本项目
- 分享给需要的朋友
- 在社交媒体推荐

## 📝 提交数据

### 黑客松数据

在 `data/hackathons.json` 中添加：

```json
{
  "title": "活动名称",
  "time": "2026.05.01-2026.05.30",
  "location": "城市/地区",
  "organizer": "主办方",
  "link": "https://活动链接",
  "source": "数据来源"
}
```

**必填字段**：
- `title`: 活动名称
- `link`: 活动链接
- `source`: 数据来源

**选填字段**：
- `time`: 活动时间
- `location`: 活动地点
- `organizer`: 主办方

### 孵化器数据

在 `data/incubators.json` 中添加：

```json
{
  "name": "孵化器名称",
  "location": "所在城市",
  "address": "详细地址",
  "type": "孵化器类型",
  "focus": "关注领域",
  "website": "https://官网",
  "contact": "联系方式",
  "services": ["服务1", "服务2"],
  "source": "数据来源"
}
```

**必填字段**：
- `name`: 孵化器名称
- `location`: 所在城市
- `source`: 数据来源

## 🔧 开发指南

### 环境准备

```bash
# 克隆项目
git clone https://github.com/AIPMAndy/FreeFound.git
cd FreeFound

# 安装依赖
pip install requests beautifulsoup4

# 运行测试
python collector.py
```

### 添加新数据源

1. 在 `collector.py` 中添加新的收集方法：

```python
def collect_new_source(self):
    """收集新数据源"""
    print("📍 收集新数据源...")
    
    url = "https://new-source.com/api"
    
    try:
        resp = requests.get(url, headers=self.headers, timeout=10)
        data = resp.json()
        
        for item in data:
            self.hackathons.append({
                "title": item['title'],
                "link": item['url'],
                "source": "新数据源"
            })
        
        print(f"✅ 新数据源收集完成\n")
        
    except Exception as e:
        print(f"✗ 新数据源收集失败: {e}\n")
```

2. 在 `main()` 函数中调用：

```python
hackathon_collector.collect_new_source()
```

### 代码规范

- 使用 Python 3.9+
- 遵循 PEP 8 代码风格
- 添加必要的注释和文档字符串
- 处理异常情况

### 提交规范

**Commit Message 格式**：

```
<type>: <subject>

<body>
```

**Type 类型**：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建/工具相关

**示例**：

```
feat: 添加掘金黑客松数据源

- 实现掘金 API 调用
- 添加数据格式转换
- 更新文档说明
```

## 🚀 Pull Request 流程

1. **Fork 项目**
   
   点击右上角 Fork 按钮

2. **创建分支**
   
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **提交更改**
   
   ```bash
   git add .
   git commit -m "feat: 你的功能描述"
   ```

4. **推送分支**
   
   ```bash
   git push origin feature/your-feature-name
   ```

5. **创建 Pull Request**
   
   - 进入你的 Fork 仓库
   - 点击 "New Pull Request"
   - 填写 PR 描述
   - 等待 Review

### PR 描述模板

```markdown
## 变更类型
- [ ] 新功能
- [ ] Bug 修复
- [ ] 文档更新
- [ ] 数据补充

## 变更说明
简要描述你的变更内容

## 测试
说明如何测试你的变更

## 截图（如适用）
添加相关截图

## Checklist
- [ ] 代码遵循项目规范
- [ ] 已添加必要的注释
- [ ] 已更新相关文档
- [ ] 已测试变更内容
```

## ✅ 数据质量标准

### 黑客松数据

- ✅ 活动真实存在
- ✅ 链接可访问
- ✅ 时间格式统一（YYYY.MM.DD）
- ✅ 信息完整准确
- ❌ 不添加已结束超过3个月的活动
- ❌ 不添加虚假或广告信息

### 孵化器数据

- ✅ 孵化器真实存在
- ✅ 官网可访问
- ✅ 联系方式有效
- ✅ 服务内容准确
- ❌ 不添加已关闭的孵化器
- ❌ 不添加纯广告性质的内容

## 🎖️ 贡献者

感谢所有贡献者！你的名字将出现在：
- README 贡献者列表
- GitHub Contributors 页面
- 项目网站致谢页面

## 📞 联系我们

- GitHub Issues: [提交问题](https://github.com/AIPMAndy/FreeFound/issues)
- GitHub Discussions: [参与讨论](https://github.com/AIPMAndy/FreeFound/discussions)
- Email: 通过 GitHub Profile 联系维护者

## 📄 行为准则

参与本项目即表示你同意遵守我们的行为准则：

- 尊重所有贡献者
- 接受建设性批评
- 关注项目目标
- 保持友好和专业

---

再次感谢你的贡献！🎉

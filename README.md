# rongxian-skills

我的各种 Codex / Agent skills。

## 活动文档类

### 活动方案

路由 skill。用户只说“活动方案 / 策划案 / 执行方案”但没有明确活动规模时，用它判断应该进入小活动还是大活动。

- 路径：[`activity-plan/`](activity-plan/)
- 分流：半天/一天转 `小活动方案`，两天及以上或多模块复杂活动转 `大活动方案`

### 小活动方案

半天或一天周期的小型活动方案，适合沙龙、Workshop、分享会、单日路演、校园单日活动、企业内训单场活动。

- 路径：[`small-activity-plan/`](small-activity-plan/)
- 重点：现场流程、人员分工、物料清单、预算、执行 SOP、风险预案

### 飞书小型活动

飞书文档中的半天或一天小型活动交付文档，适合需要直接创建、更新和验证 Feishu/Lark 文档的沙龙、圆桌、开放麦、Workshop、路演、分享会。

- 路径：[`feishu-small-activity/`](feishu-small-activity/)
- 重点：飞书 DocxXML 结构、callout/table/grid/checkbox/whiteboard、确定版写作口径、fetch 验证

### 大活动方案

两天及以上的大型活动方案，适合峰会、展会、科技节、黑客松、赛事、训练营、活动周和多方协同项目。

- 路径：[`large-activity-plan/`](large-activity-plan/)
- 重点：跨天时间轴、活动模块、组织架构、综合保障、招商传播、预算和验收成果

### 文旅 AIGC 黑客松方案

面向景区、文旅项目和地方文旅部门的 AIGC 创作者黑客松、AI 文旅内容赛事与文创 IP 共创赛。

- 路径：[`design-cultural-tourism-aigc-hackathon/`](design-cultural-tourism-aigc-hackathon/)
- 重点：线上报名筛选、双赛道独立评奖、具体作品交付、景区价值、最低刚性成本与完整执行预算

### AI课程培训

AI Workshop、企业/校园 AI 培训、课程大纲、课表、实训任务、讲师配置、培训报价和交付方案。

- 路径：[`ai-course-training/`](ai-course-training/)
- 重点：课程模块、教学目标、实操任务、学员产出、讲师助教配置、验收方式

### 活动合同

活动合同、服务协议、执行合同、培训服务合同、报价条款、付款验收、违约责任、保密、知识产权和取消改期。

- 路径：[`activity-contract/`](activity-contract/)
- 重点：服务范围、费用付款、验收标准、双方责任、风险条款和附件一致性

## 工具层

### frontend-product-review

Web 前端产品修改建议 skill。用于把页面建议写到导航、顶部、筛选、列表、按钮、侧板、弹窗和点击结果的粒度，避免只给抽象产品判断。

- 路径：[`frontend-product-review/`](frontend-product-review/)
- 适用：Web 产品评审、前端页面改造建议、交互路径梳理、页面级实现规划

### docx-precise-editor-codex

Codex 版本的底层 Word `.docx` 精准编辑工具。它不再负责判断活动业务场景，只负责在需要保留 Word 版式时做低层文本替换和表格编辑。

- 路径：[`docx-precise-editor-codex/`](docx-precise-editor-codex/)
- 适用：已有 Word 文件的局部修改、保留封面/样式/图片/表格结构、字节级文本替换
- 被复用：`小活动方案`、`大活动方案`、`AI课程培训`、`活动合同`

### customer-case

客户案例、服务案例、商业合作材料和能力展示材料，适合需要脱敏或正式对外表达的项目复盘。

- 路径：[`customer-case/`](customer-case/)

### manufacturing-ai-flow

中小制造业 AI 生产流转、MES/轻量 ERP 试点、工单、工艺参数、风险日报和实施路线设计。

- 路径：[`manufacturing-ai-flow/`](manufacturing-ai-flow/)

### frontend-product-review

Web 产品页面评审和前端改造建议，具体到页面模块、按钮、筛选、列表、侧板和点击结果。

- 路径：[`frontend-product-review/`](frontend-product-review/)

### personal-ppt

陈容贤个人介绍、创业经历、企业 AI 分享和服务转化类 PowerPoint 材料。

- 路径：[`personal-ppt/`](personal-ppt/)

## 内容与研究类

### dong-kehan

董克汉创作者档案分析、审美偏好、价值地图和语言风格提取。

- 路径：[`dong-kehan/`](dong-kehan/)

### follow-builders

追踪 AI Builder 在 X/Twitter 和 YouTube 的动态，整理成中文 AI 行业摘要。

- 路径：[`follow-builders/`](follow-builders/)

## 飞书画板类

### design-lark-chart

把业务需求转成可编辑、可质检的飞书架构图、流程图、泳道图、时序图、思维导图和自由画图结果。

- 路径：[`design-lark-chart/`](design-lark-chart/)

## 兼容版本

### docx-precise-editor-workbuddy

WorkBuddy 版本。保留 WorkBuddy frontmatter 和工具授权字段，适合安装到 `~/.workbuddy/skills/`。

- 路径：[`docx-precise-editor-workbuddy/`](docx-precise-editor-workbuddy/)

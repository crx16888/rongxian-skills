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

### 大活动方案

两天及以上的大型活动方案，适合峰会、展会、科技节、黑客松、赛事、训练营、活动周和多方协同项目。

- 路径：[`large-activity-plan/`](large-activity-plan/)
- 重点：跨天时间轴、活动模块、组织架构、综合保障、招商传播、预算和验收成果

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

## 兼容版本

### docx-precise-editor-workbuddy

WorkBuddy 版本。保留 WorkBuddy frontmatter 和工具授权字段，适合安装到 `~/.workbuddy/skills/`。

- 路径：[`docx-precise-editor-workbuddy/`](docx-precise-editor-workbuddy/)

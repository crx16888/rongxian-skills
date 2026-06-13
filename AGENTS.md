# AGENTS.md

本仓库保存用户自用的 Codex / Agent skills。维护目标是让每个 skill 的触发边界清楚、文档短而可执行，并且能被安装工具和 Codex 正确识别。

## 协作原则

- 用户偏实践和结果导向。修改本仓库时优先把 skill 真正落盘、验证、提交，而不是只给建议。
- 用户明确给出的仓库、路径、文件名和 skill 名称是稳定标识，优先级高于本机当前配置或旧记忆。
- 如果需求可能失败，直接指出真正阻塞点，例如缺少文件、GitHub 权限不可用、skill metadata 无法解析、安装列表不可见。
- 除非用户明确要求重构，否则保持改动范围小：只改相关 skill、README、AGENTS.md 或必要的 metadata。

## 仓库结构

根目录下每个 skill 一个目录：

- `activity-plan/`：活动方案路由 skill，只负责把活动方案分流到小活动或大活动。
- `small-activity-plan/`：半天或一天周期的小型活动方案。
- `large-activity-plan/`：两天及以上或多模块复杂的大型活动方案。
- `ai-course-training/`：AI 课程培训、Workshop、课表、实训任务和培训交付。
- `activity-contract/`：活动合同、服务协议、付款验收和风险条款。
- `docx-precise-editor-codex/`：Codex 版底层 Word `.docx` 精准编辑工具。
- `docx-precise-editor-workbuddy/`：WorkBuddy 兼容版本。

每个 Codex skill 至少应包含：

```text
<skill-name>/
├── SKILL.md
└── agents/
    └── openai.yaml
```

有脚本、参考资料或模板时，可增加：

```text
scripts/
references/
assets/
```

## Skill 边界

活动文档类 skill 必须保持互斥边界：

- 半天或一天周期的小型活动，使用 `小活动方案`。
- 两天及以上，或多模块、多场地、多组织方、多阶段筹备的大型活动，使用 `大活动方案`。
- 用户只说“活动方案 / 策划案 / 执行方案”但规模不清楚，先使用 `活动方案` 做路由。
- 核心是 AI 课程、培训体系、课表、实训任务、讲师配置，使用 `AI课程培训`。
- 核心是合同、服务协议、付款、验收、违约、保密、知识产权，使用 `活动合同`。
- 核心只是修改已有 Word 且保留版式，业务 skill 先判断场景，再复用 `docx-precise-editor-codex` 的脚本和规则。

不要让 `docx-precise-editor-codex` 重新变成活动业务总入口。它只负责低层 DOCX 编辑，不负责活动方案、培训或合同的业务写法。

## 编写规范

`SKILL.md` 必须包含 YAML frontmatter：

```yaml
---
name: skill名称
description: 说明何时使用，何时不要使用，必要时写清替代 skill
---
```

正文建议包含：

- `触发边界`
- `工作流`
- `推荐结构` 或 `输出结构`
- `写作口径`

写作要求：

- `description` 要足够清楚，因为这是 Codex 判断是否触发 skill 的主要依据。
- 保持短而可执行，避免把通用常识塞进 skill。
- 涉及多个场景时，优先拆成不同 skill，而不是在一个 skill 里写巨型规则。
- 新增或修改 skill 后，同步更新 `agents/openai.yaml`。
- 新增目录后，同步更新 `README.md` 的分类展示。

## DOCX 编辑约束

处理 Word 文档相关能力时，遵守 `docx-precise-editor-codex/` 的低层规则：

- 不要用通用 `unpack -> 改 XML -> pack` 流程重排整份 DOCX。
- 优先只修改 `word/document.xml` 中授权的文本内容。
- 修改已有文件前应备份。
- 尽量保留封面、样式、图片、表格结构。
- 表格是高风险区域，改完要核对行列结构。

## 验证

修改 skill 后至少做以下检查：

```bash
python3 - <<'PY'
from pathlib import Path

for p in Path('.').glob('*/SKILL.md'):
    text = p.read_text()
    assert text.startswith('---\n'), p
    _, fm, body = text.split('---', 2)
    fields = {}
    for line in fm.strip().splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            fields[k.strip()] = v.strip()
    assert fields.get('name'), p
    assert fields.get('description'), p
    assert body.strip(), p
    print('OK', p, fields['name'])
PY
```

如果在本机全局 skill 目录也同步了 skill，额外检查：

```bash
npx skills list -g -a codex --json
```

官方 `quick_validate.py` 可能依赖 `PyYAML`。如果当前 Python 环境缺少该依赖，不要为了验证随意改全局环境；可先用上面的轻量 frontmatter 检查和 `npx skills list` 验证可见性。

## Git 工作流

默认在 `main` 上维护，除非用户要求开分支或 PR。

常规流程：

```bash
git status --short --branch
git pull --ff-only
# edit files
git diff --stat
git diff
git add <changed-files>
git commit -m "<clear commit message>"
git push origin main
```

推送前确认：

- 工作区没有无关改动被误加入。
- README 分类和实际目录一致。
- 新增 skill 有 `SKILL.md` 和 `agents/openai.yaml`。
- 如果同步了本地 `~/.codex/skills/`，本地列表能看到对应 skill。

## GitHub 仓库

当前目标仓库：

```text
https://github.com/crx16888/rongxian-skills
```

用户要求“上传到我的 GitHub”时，优先使用这个仓库，除非用户提供新的明确仓库链接。


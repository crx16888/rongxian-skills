---
name: docx-precise-editor
description: 精确编辑 Word 活动方案和提案类 .docx 文档，尽量只修改授权内容并保留原有版式。Use when Codex needs to modify activity plans, event proposals, Hackathon plans, campus activity方案, Word/docx text, responsibility descriptions, budgets, pricing tables, material-execution scope, tax/payment terms, or append rows while preserving formatting.
---

# docx-precise-editor · Codex 活动方案精准编辑器

> 核心原则：**只改你批准的，绝不多碰一个字节。**

## 为什么不用通用 docx 流程

标准流程 `unpack → 改 XML → pack` 会**重新格式化整个文档的 XML**，连封面、页眉、未授权的章节都会被自动重构。你改三个字，它给你翻修全屋。

本 Skill 用 `zipfile` 直接操作 ZIP 包，字节级精准替换。封面、样式、图片 —— 原封不动。

## 技术铁律

1. **不 unpack、不 pack** —— 用 Python `zipfile` 直接读写 `word/document.xml`
2. **只改 `<w:t>` 文本内容** —— 不改任何 XML 结构、属性、run
3. **原地编辑** —— 永远在源文件上改，不另存新文件
4. **改前备份** —— 自动存 `.docx.backup`，可随时回滚
5. **不动封面** —— 前 5000 字节必须与备份逐字节一致

## 三步工作流

```
1. 备份源文件          2. 字节级精准替换              3. 验证 + 展示
   docx → .backup         zipfile 只读 document.xml     封面未碰✓ 结构完好✓
```

## 开场声明

每次使用本 skill，先告诉用户：

```text
使用 skill：docx-precise-editor
路径：/Users/linyao/.codex/skills/docx-precise-editor/SKILL.md
原因：<一句话>
```

## 活动方案常见编辑模式

| 模式 | 原始 | 改为 |
|------|------|------|
| **内容具体化** | 为学校形成产教融合成果 | 1）教学成果转化 2）校企合作里程碑 3）双创教育闭环 |
| **职责边界澄清** | 协助搭建报名、分组 | 负责分组签到和现场执行（学生名单由甲方提供） |
| **案例行增补** | 表格 3 行 | 表格 4 行（追加一行，列宽字体对齐） |
| **数据更新** | 预算 50,000 | 预算 80,000 |

## 报价方案编辑

如果用户修改报价、套餐、物料、税费、付款、多场次折扣，先读：

`references/activity-quote-rules.md`

报价表格是高风险区域：

- 不要把整张表的文本合并到一个 `<w:t>` 或一个单元格里。
- 改表格时按 `w:tr` / `w:tc` 单元格处理，保证每行列数一致。
- 改完必须抽取表格行列核对，例如打印每行 cell 文本。
- “不包含”在总览表里用 `／`，不要写成长文本。
- 重点差异要加粗：套餐名、价格、AI Workshop、物料执行边界、税费、付款方式、多场次折扣。

## 字体标准（Word 合作文档级）

活动方案面向外部合作方，字体需保证对方打开即可编辑：

| 用途 | 字体 | 字号 | 加粗 |
|------|------|------|------|
| 封面标题 | 微软雅黑 | 二号(22pt) | ✔ |
| 封面副标题 | 微软雅黑 | 小三(15pt) | — |
| 一级标题 | 黑体 | 三号(16pt) | ✔ |
| 二级标题 | 黑体 | 四号(14pt) | ✔ |
| 正文 | 宋体 | 小四(12pt) | — |
| 表格内容 | 宋体 | 五号(10.5pt) | — |
| 关键数字 | 宋体 | 小四(12pt) | ✔ |

> 不使用 Noto Sans CJK SC、思源等对方可能未安装的字体。文档发给任何人，打开即所见。

## 使用脚本

从当前 skill 目录解析脚本路径，例如 `/Users/crx/.codex/skills/docx-precise-editor/scripts/edit_docx.py`。不要假设用户当前工作目录就在 skill 目录中。

```bash
# 字节级编辑（不改任何 XML 结构）
python3 scripts/edit_docx.py <文件路径> <old_text> <new_text>

# 追加案例表格行
python3 scripts/append_table_row.py <文件路径> <行数据JSON> <表格内定位文字>
```

## 目录

```
docx-precise-editor/
├── SKILL.md                          # 本文件
├── scripts/
│   ├── edit_docx.py                  # 字节级文本替换
│   └── append_table_row.py           # 表格尾追加行
└── references/
    └── style-guide.md                # 字体与排版规范
    └── activity-quote-rules.md       # 活动报价口径
```

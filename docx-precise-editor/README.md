# docx-precise-editor

> 精确编辑 Word 活动方案 —— 只改你说改的，绝不多碰一个字节。

## 为什么需要它

标准 docx 处理流程 `unpack → 改 XML → pack` 会重新格式化整个文档。你改三个字，它把封面、样式、页眉全部重构一遍。发给合作方打开一看，格式全跑了。

这个工具用 `zipfile` 直接操作 docx 内部的 XML，**字节级精准替换**。封面、图片、样式 —— 原封不动。

## 快速开始

```bash
# 替换一段文字
python3 scripts/edit_docx.py 活动方案.docx "原文字" "新文字"

# 给案例表格加一行
python3 scripts/append_table_row.py 活动方案.docx '["案例名","形式","内容"]' "上一行关键词"
```

自动备份 `.docx.backup`，改错了随时回滚。

## 适用场景

| ✅ 适用 | ❌ 不适用 |
|---------|----------|
| 改已有活动方案中的某段文字 | 从零创建新文档（用 python-docx） |
| 把笼统描述改成具体条款 | 改表格结构（删列/合并单元格） |
| 在案例表末尾追加一行 | 改封面设计 |
| 修正职责边界描述 | 改图表/图片 |

## 文件结构

```
├── SKILL.md                    # WorkBuddy Skill 定义
├── scripts/
│   ├── edit_docx.py            # 字节级文本替换
│   └── append_table_row.py     # 表格尾追加行
└── references/
    └── style-guide.md          # 合作文档排版规范
```

## 字体选择原则

| 字体 | 为什么用 |
|------|---------|
| 宋体 | Windows/macOS 100% 自带 |
| 黑体 | 标题首选，全平台可用 |
| 微软雅黑 | 封面标题，清晰现代 |

不用思源、苹方、方正 —— 发给合作方打不开等于白做。

## 作为 WorkBuddy Skill 安装

```bash
cp -r docx-precise-editor ~/.workbuddy/skills/
```

之后对 WorkBuddy 说「帮我把活动方案第 3 段改具体一点」即可触发。

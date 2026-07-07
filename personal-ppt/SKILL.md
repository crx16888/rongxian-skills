---
name: personal-ppt
description: Create, update, restructure, polish, and verify Chen Rongxian's personal introduction PowerPoint materials, including entrepreneurship experience, Flux Nanckathon/Nankesong, Zhuandian Technology FDE, enterprise AI sharing, BP-style business logic, training/service conversion pages, WeChat QR/contact endings, and P1-style deck edits. Use when the user says "我的个人PPT", "个人材料介绍PPT", "创业经历PPT", "Flux南客松PPT", "转点科技FDE", "企业AI分享", or asks to continue editing the current personal PPT deck.
---

# Personal PPT

## Core Workflow

1. Treat the current deck as the source of truth. Read the latest PPT before editing, especially after the user says they made manual changes.
2. Load the `presentations` skill for any `.pptx` editing and use its artifact-tool workflow. Do not use `python-pptx`.
3. Work directly on the target deck unless the user asks for a separate copy. Create a timestamped backup before modifying.
4. Inspect the target slide text and export a before preview when layout matters. Edit only the requested slide(s) or section.
5. Preserve the existing P1-inspired style: white background, bright blue hierarchy, restrained black/gray body copy, small footer/page number, clean geometry, and editable PowerPoint objects.
6. Export after-preview images for edited slides. Run a narrow verification; if running whole-deck checks, distinguish pre-existing warnings from the current edit.
7. Save both the local target and iCloud mirror when both exist. Clean transient `.inspect.ndjson` files from user-facing folders.
8. Report the edited slide(s), saved paths, backup path, and any verification warnings briefly.

## Read The Deck Profile

Before substantive deck edits, read `references/deck-profile.md`. It contains the current target file paths, deck structure, style tokens, content framing, and recurring copy constraints.

Use it especially when:

- Adding or changing Part 1 entrepreneurship pages.
- Editing Flux 南客松 community, activity, or partnership pages.
- Editing 转点科技 FDE / BP logic / enterprise AI pages.
- Updating the agenda, self-introduction, ending, or WeChat QR pages.
- Reordering sections or adding pages that must match the current narrative.

## Narrative Defaults

Use this deck as a personal-business material, not a generic resume deck.

- Part 1 explains why the speaker moved from campus entrepreneurship into technology entrepreneurship.
- Flux 南客松 explains how the speaker aggregates AI Builder communities, events, partners, and training opportunities.
- 转点科技 FDE explains how community, training, product/service delivery, and enterprise AI automation convert into business value.
- Enterprise-facing Part 4 should be usable for business-owner sharing and should help convert FDE and training services.

Keep copy audience-facing. Do not include production notes, internal instructions, or artificial section labels unless the deck already uses them.

## Editing Guardrails

- Preserve user manual edits. If the user says they changed the PPT, re-read the latest file and avoid using stale extracted text.
- Avoid inventing achievements, client names, or metrics. Use existing deck/source material or state uncertainty.
- Keep descriptions large enough for projection. Prefer shortening text over shrinking below the deck's current body scale.
- Avoid making one dense wall of text. Use the deck's existing P1-style structures: large title, two/three columns, short proof points, bottom synthesis sentence, or image collage.
- If replacing page structure, keep footer text and page number consistent.
- For image-heavy pages, reuse existing deck/PDF/photo assets when available and verify crops visually.

## Typical Requests

- "读取最新 PPT，然后改第 2 页今天分享内容。"
- "Part 4 增加企业 AI 应用案例页。"
- "把这页改成三层逻辑：个人工具使用、内部流程管理、业务流嵌入。"
- "丰富我的创业经历 Part 1。"
- "把 Flux 南客松介绍页做成更适合对外分享的版本。"
- "结尾加我的微信二维码。"

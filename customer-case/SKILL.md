---
name: customer-case
description: Use when creating, rewriting, polishing, or designing customer cases, service cases, business cooperation materials, proposal decks, capability showcases, or state-owned-enterprise style reporting materials; especially when client names must be anonymized.
---

# Customer Case

## Core Principle

Turn raw project details into credible service cases: anonymized client context, clear business problem, concrete service path, visible deliverables, and verifiable business value. For external-facing or state-owned-enterprise reporting, prefer restrained, orderly, institutional language and design.

## Triggered Workflows

Use this skill for:

- Customer case decks, business case pages, service capability showcases, proposal appendices, and prior-project proof pages.
- Materials for government, state-owned enterprise, bank, industrial group, or formal B2B reporting contexts.
- Any case material containing real client names, city names, project names, logos, screenshots, or transaction-sensitive details.
- Commercial narrative upgrades where the user asks for “美观漂亮、工整、商务、国企汇报、对外、服务案例、商业合作、客户案例”.

When the output is a PPTX, also use the presentation workflow/tooling required by the environment.

## Non-Negotiables

- Anonymize obvious client identifiers unless the user explicitly asks to keep them. Replace names such as banks, listed companies, government units, or branded customers with forms like “某城商行”, “某区域酒业集团”, “某省属制造企业”, “某大型能源集团”.
- Do not invent quantified outcomes. Keep source metrics when present; otherwise use process and capability language such as “形成试点闭环”, “支撑预算复盘”, “建立可审计运营机制”.
- Preserve business credibility. Do not over-market with exaggerated claims, slogans, fake logos, fake screenshots, or unsupported rankings.
- Separate “source evidence” from “target deliverable”. Edit the intended target artifact directly when the user asked for an upgraded file.
- Report real blockers: unreadable source files, missing permissions, absent fonts/rendering tools, or dynamic shells that do not expose content.

## Case Structure

Prefer this structure for each case page or section:

1. **匿名客户与场景**: industry + organization type + business scenario.
2. **客户问题**: 3 concise pain points from different roles such as management, business department, IT, sales, operation, compliance.
3. **我方服务**: 3 concrete service actions, not generic capability labels.
4. **落地路径**: 4-6 step implementation chain, e.g. 数据盘点 -> 用户分层 -> 试点投放 -> 线索派发 -> 复盘扩量.
5. **交付物**: named outputs such as data asset list, segmentation rules, dashboard, lead list, audit log, pilot report.
6. **验收与价值**: metrics if available; otherwise describe the decision, governance, efficiency, conversion, or risk-control value enabled.

Recommended one-line value statement:

```text
商务价值：把[原有状态/问题]转化为[可执行能力]，支撑[管理决策/业务增长/风险治理]。
```

## Language Rules

- Use “面向…提供…”, “以…方式…”, “形成…闭环”, “支撑…复盘/扩展/治理”, “满足…要求” for formal B2B tone.
- Prefer “我方服务” over “我们做了什么” in formal materials.
- Prefer “试点、闭环、看板、清单、规则、机制、复盘、验收、扩量、审计” for deliverable-oriented wording.
- Avoid consumer-marketing words like “爆款、颠覆、超强、极致、革命性”.
- Keep each bullet short enough for slide layout. If text wraps too much, shorten wording before shrinking font.

## Visual Direction For Formal Decks

- Use restrained palettes: deep navy, institutional gray, white, and a small gold accent. Avoid loud gradients, cartoon icons, decorative blobs, and startup-style marketing pages.
- Keep the page grid stable: left case rail or top title band, three balanced columns for problem/service/value, bottom path or deliverables strip.
- Use consistent page numbers, case labels, section badges, separators, and metric cards.
- Keep metrics visually stable. If symbols or long Chinese terms wrap poorly, use shorter equivalent labels while preserving meaning.
- Do visual QA from rendered previews, not only extracted text. Check overlap, clipping, awkward line breaks, and leftover client identifiers.

## Anonymization Patterns

| Source type | Safer wording |
| --- | --- |
| 南京银行 / local named bank | 某城商行 / 某区域银行 / 某金融机构 |
| 今世缘 / named alcohol brand | 某区域酒业集团 / 某白酒企业 |
| Named government bureau | 某市级主管部门 / 某省级政务单位 |
| Named SOE group | 某省属集团 / 某大型能源集团 |
| Named SaaS or platform customer | 某大型企业客户 / 某集团型客户 |

Keep industry and scenario specificity where possible. Anonymization should reduce identity risk without flattening the case into vague claims.

---
name: pm-master
description: Route product work to the installed task skills. Use for pm-master, 产品总控, 选技能 or a requested complete workflow. Do not add steps to a single-task request.
---

# 日常总控

先识别用户要的交付物，再选一个入口。用户点名旧技能时查 references/aliases.json，使用对应的新入口与具体模式；不要求用户重新学习名字。

| 问题 | 入口 |
|---|---|
| PRD、故事地图、验收 | pm-requirements |
| 问卷、访谈、画像、反馈 | pm-research |
| 机会、方案、假设验证 | pm-discovery |
| 数据、留存、指标、埋点 | pm-data |
| A/B 设计或结果 | pm-experiments |
| 排优先级 | pm-priorities |
| OKR、路线图、排期 | pm-planning |
| 竞品 | pm-competition |
| 战略、市场、商业画布 | pm-strategy |
| 复购、获客、定价、商业化 | pm-growth |
| 评审、风险预演、复盘 | pm-review |
| 纪要、发布、润色、命名 | pm-communication |
| 专家视角与价值判断 | pm-advisory-board |
| 截图 HTML / .pen / 网页项目 | pm-image2proto / pm-image2pencil / pm-url2proto |

只有用户要求完整链路，或交付物确实依赖多个步骤时才编排。交接包括目标、事实、硬约束、已决事项、未决项、产物路径；总控也必须推进执行，不以“仅路由”为理由停止。工具未安装或不在会话中时说明具体缺口，完成可做部分。

## 执行约定

- 根据用户的问题只选相关模式，读取下方对应参考；不把所有方法串成固定流程。
- 已确认的业务规则和用户指定格式优先。事实、建议、假设与待确认项分开；缺人数、效果、成本或工时不编数。
- C 端场景检查转化、留存、退款、毛利与履约的取舍，选择实际受影响的指标；不为小改动扩写全套材料。
- 输入充分就执行。缺硬约束时先完成独立可做部分，再集中补问；普通草稿不重复申请批准。
- 用户要求文件时实际创建文件，使用当前可用的平台工具。未写入远端、未运行或未验收时不能宣称成功。

## 按需参考

- [日常总控方法](references/routing.md)
- [旧名与新入口映射](references/aliases.json)

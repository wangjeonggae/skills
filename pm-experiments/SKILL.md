---
name: pm-experiments
description: Design and analyze randomized product experiments with sample sizes and decision rules. Use for A/B测试, 实验方案, 样本量, SRM or 实验结果. Do not extend tests to chase significance.
---

# 实验设计与分析

区分设计尚未启动的实验和分析已有结果，共用 references/statistics.md 的统计规则。计算二项指标可用 scripts/experiment_stats.py；连续、比值、聚类指标须匹配分析单位和方差方法。

预先确定随机单位、比较集合、主指标、业务收益门槛、护栏恶化界限、窗口、样本、停止规则。MDE 是设计灵敏度，不自动等于上线收益门槛。

结果报告绝对差、相对差、区间、检验方法和限制。主指标显著也需核退款、误加购、毛利和履约护栏；护栏不显著不能证明安全。不依据中途 p 值临时延长、换指标或删样本。

## 执行约定

- 根据用户的问题只选相关模式，读取下方对应参考；不把所有方法串成固定流程。
- 已确认的业务规则和用户指定格式优先。事实、建议、假设与待确认项分开；缺人数、效果、成本或工时不编数。
- C 端场景检查转化、留存、退款、毛利与履约的取舍，选择实际受影响的指标；不为小改动扩写全套材料。
- 输入充分就执行。缺硬约束时先完成独立可做部分，再集中补问；普通草稿不重复申请批准。
- 用户要求文件时实际创建文件，使用当前可用的平台工具。未写入远端、未运行或未验收时不能宣称成功。

## 按需参考

- [实验设计与分析方法](references/statistics.md)

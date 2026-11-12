#!/usr/bin/env python3
"""Independent binary outcomes only; large-sample, fixed-window approximations."""
import argparse
import json
import math
from statistics import NormalDist

NORMAL = NormalDist()


def sample_size(p0, p1, alpha=0.05, power=0.8, comparisons=1):
    if not 0 < p0 < 1 or not 0 < p1 < 1 or p0 == p1:
        raise ValueError("Require unequal probabilities strictly between 0 and 1")
    if not 0 < alpha < 1 or not 0.5 < power < 1 or not isinstance(comparisons, int) or comparisons < 1:
        raise ValueError("Invalid alpha, power, or comparison count")
    adjusted = alpha / comparisons
    za = NORMAL.inv_cdf(1 - adjusted / 2)
    zb = NORMAL.inv_cdf(power)
    pbar = (p0 + p1) / 2
    n = (za * math.sqrt(2*pbar*(1-pbar)) + zb * math.sqrt(p0*(1-p0)+p1*(1-p1))) ** 2 / (p1-p0) ** 2
    return {"per_group": math.ceil(n), "unrounded": n, "alpha_per_comparison": adjusted,
            "absolute_mde": abs(p1-p0), "relative_mde": abs(p1-p0)/p0,
            "method": "equal allocation independent binary normal approximation"}


def analyze(n0, x0, n1, x1, alpha=0.05, comparisons=1):
    if min(n0, n1) <= 0 or not (0 <= x0 <= n0 and 0 <= x1 <= n1):
        raise ValueError("Require positive sample counts and valid success counts")
    if not 0 < alpha < 1 or comparisons < 1:
        raise ValueError("Invalid alpha or comparison count")
    p0, p1 = x0/n0, x1/n1
    pooled = (x0+x1)/(n0+n1)
    if min(x0, n0-x0, x1, n1-x1) < 10:
        raise ValueError("Normal approximation unsuitable; use Wilson/Newcombe or an exact method")
    se_null = math.sqrt(pooled*(1-pooled)*(1/n0+1/n1))
    z = (p1-p0)/se_null
    p = math.erfc(abs(z)/math.sqrt(2))
    se_ci = math.sqrt(p0*(1-p0)/n0 + p1*(1-p1)/n1)
    critical = NORMAL.inv_cdf(1-alpha/comparisons/2)
    return {"control": p0, "variant": p1, "difference": p1-p0,
            "relative_lift": (p1-p0)/p0 if p0 else None,
            "p_value_raw": p, "p_value_bonferroni": min(1, p*comparisons),
            "difference_interval": [p1-p0-critical*se_ci, p1-p0+critical*se_ci],
            "interval_alpha": alpha/comparisons,
            "method": "pooled two-sided z test and unpooled Wald difference interval",
            "decision": "Requires experiment validity, preset business threshold and mature guardrails"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["size", "analyze"])
    parser.add_argument("--p0", type=float)
    parser.add_argument("--p1", type=float)
    parser.add_argument("--n0", type=int)
    parser.add_argument("--x0", type=int)
    parser.add_argument("--n1", type=int)
    parser.add_argument("--x1", type=int)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--power", type=float, default=0.8)
    parser.add_argument("--comparisons", type=int, default=1)
    args = parser.parse_args()
    try:
        if args.mode == "size":
            if args.p0 is None or args.p1 is None:
                parser.error("size requires --p0 and --p1")
            result = sample_size(args.p0, args.p1, args.alpha, args.power, args.comparisons)
        else:
            if any(x is None for x in [args.n0, args.x0, args.n1, args.x1]):
                parser.error("analyze requires --n0 --x0 --n1 --x1")
            result = analyze(args.n0, args.x0, args.n1, args.x1, args.alpha, args.comparisons)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

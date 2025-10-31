"""Deterministic financial ratio helpers.

The math lives in module-level functions so it can be unit-tested without
any LLM or network.
"""

from __future__ import annotations


def current_ratio(current_assets: float, current_liabilities: float) -> float:
    if current_liabilities == 0:
        raise ValueError("current_liabilities must be non-zero")
    return current_assets / current_liabilities


def debt_to_equity(total_debt: float, total_equity: float) -> float:
    if total_equity == 0:
        raise ValueError("total_equity must be non-zero")
    return total_debt / total_equity


def gross_margin(revenue: float, cogs: float) -> float:
    if revenue == 0:
        raise ValueError("revenue must be non-zero")
    return (revenue - cogs) / revenue


def cagr(begin_value: float, end_value: float, years: float) -> float:
    if begin_value <= 0 or years <= 0:
        raise ValueError("begin_value and years must be positive")
    return (end_value / begin_value) ** (1 / years) - 1


def return_on_equity(net_income: float, shareholder_equity: float) -> float:
    if shareholder_equity == 0:
        raise ValueError("shareholder_equity must be non-zero")
    return net_income / shareholder_equity


def quick_ratio(current_assets: float, inventory: float,
                current_liabilities: float) -> float:
    if current_liabilities == 0:
        raise ValueError("current_liabilities must be non-zero")
    return (current_assets - inventory) / current_liabilities

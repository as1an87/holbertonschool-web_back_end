#!/usr/bin/env python3
"""Function"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return"""
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function


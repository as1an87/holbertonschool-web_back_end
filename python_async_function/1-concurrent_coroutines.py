#!/usr/bin/env python3
"""Function"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return"""
    i = [wait_random(max_delay) for _ in range(n)]
    i = asyncio.as_completed(i)
    d = [await j for j in i]
    return d

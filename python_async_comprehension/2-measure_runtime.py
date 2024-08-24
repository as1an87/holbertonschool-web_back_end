#!/usr/bin/env python3
import asyncio
import time
from 1_async_comprehension import async_comprehension
"""
Function
"""


async def measure_runtime() -> float:
    """
    Return
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    total_runtime = time.perf_counter() - start_time
    return total_runtime

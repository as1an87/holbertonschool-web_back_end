#!/usr/bin/env python3
"""Function"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return"""
    futures = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await future for future in asyncio.as_completed(futures)]
    return delays

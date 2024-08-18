#!/usr/bin/env python3
"""Function"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return"""
    delays = await asyncio.gather(*(wait_gather(max_delay) for _ in range(n)))
    return sorted(delays)

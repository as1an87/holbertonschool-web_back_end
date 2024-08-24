#!/usr/bin/python3 env
"""Function"""
import asyncio
import random


async def async_generator():
    """Return"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

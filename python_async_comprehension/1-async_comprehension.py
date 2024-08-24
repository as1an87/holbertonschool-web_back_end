#!/usr/bin/env python3
"""Function"""
import asyncio
from 0_async_generator import async_generator


async def async_comprehension():
    """Return"""
    return [i async for i in async_generator()]

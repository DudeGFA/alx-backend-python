#!/usr/bin/env python3
"""
    Contains function measure_runtime
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        measures runtime for the execution
        of async_comprehension four times
         in parallel using asyncio.gather
    """
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - s
    return elapsed

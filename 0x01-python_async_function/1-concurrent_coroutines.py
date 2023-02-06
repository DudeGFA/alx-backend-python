#!/usr/bin/env python3
"""
    Contains function wait_n
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        spawns wait_random n times with the specified max_delay
        and returns the list of all the delays
    """
    listOfDelays = await asyncio.gather(*tuple(map(lambda x: wait_random(max_delay), range(n))))
    return sorted(listOfDelays)

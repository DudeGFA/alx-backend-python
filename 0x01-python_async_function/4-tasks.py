"""
    Contains task task_wait_n
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        spawns task_wait_random n times with the specified max_delay
        and returns the list of all the delays
    """
    listOfDelays = await asyncio.gather(*list(map(lambda x: task_wait_random(max_delay), range(n))))
    return sorted(listOfDelays)

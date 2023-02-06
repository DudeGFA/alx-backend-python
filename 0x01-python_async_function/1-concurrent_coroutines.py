#!/usr/bin/env python3
"""
    Contains function wait_n
"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
        spawns wait_random n times with the specified max_delay
        and returns the list of all the delays
    """
    listOfDelays = []
    for i in range(n):
        listOfDelays.append(await wait_random(max_delay))
    return listOfDelays

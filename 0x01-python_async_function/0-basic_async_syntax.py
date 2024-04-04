#!/usr/bin/env python3
"""
A module for asynchronous function which
    takes an integer with 10 as default.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random amount of time up to `max_delay` seconds.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
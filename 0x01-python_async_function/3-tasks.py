#!/usr/bin/env python3
"""
module for creating asyncio Tasks that run asynchronous functions.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    returns the created Task object.
    """
    return asyncio.create_task(wait_random(max_delay))

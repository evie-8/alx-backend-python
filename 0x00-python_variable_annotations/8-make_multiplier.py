#!/usr/bin/env python3
'''Uisng a multiplier.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function using lambda.
    '''
    return lambda x: x * multiplier

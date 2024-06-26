#!/usr/bin/env python3
'''Sum of different types.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns the sum of a list of integers and floating-point numbers.
    '''
    return float(sum(mxd_lst))

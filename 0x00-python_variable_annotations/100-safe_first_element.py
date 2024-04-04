#!/usr/bin/env python3
"""
module returning the first element 
    of a list, or None if the list is empty.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function returns the first element of a sequence, or None if the
        sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

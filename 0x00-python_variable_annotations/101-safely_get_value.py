#!/usr/bin/env python3
"""
Mdoule with function for safely getting a value from
    a mapping.
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Function gets the value for a given key in a mapping
    """
    if key in dct:
        return dct[key]
    else:
        return default

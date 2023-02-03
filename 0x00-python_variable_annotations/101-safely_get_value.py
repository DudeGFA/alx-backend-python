#!/usr/bin/env python3
"""
    Contains function safely_get_value
"""

from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')
Newtype = Union[T, None]


def safely_get_value(dct: Mapping, key: Any,
                     default: Newtype = None) -> Union[Any, T]:
    """
        Safely gets a value from a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default

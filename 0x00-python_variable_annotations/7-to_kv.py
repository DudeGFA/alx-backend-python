#!/usr/bin/env python3
"""
    Contains function to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        returns a tuple containing  the string k.
        and the square of the int/float v
    """
    return (k, float(v**2))

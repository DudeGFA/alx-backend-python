#!/usr/bin/env python3
from typing import List, Union
"""
    contains function sum_mixed_list
"""


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
        returns sum of elements of a
        mixed list of ints and floats
    """
    return float(sum(mxd_list))

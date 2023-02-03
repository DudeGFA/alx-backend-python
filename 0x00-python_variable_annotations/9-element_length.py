#!/usr/bin/env python3
"""
    Contains function element_length
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        returns tuple of each element of lst
        and it's length
    """
    return [(i, len(i)) for i in lst]

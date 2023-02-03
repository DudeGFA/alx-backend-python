#!/usr/bin/env python3
"""
    contains function safe_first_element
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Augmented code with correct duck-type
        annotations
    """
    if lst:
        return lst[0]
    else:
        return None

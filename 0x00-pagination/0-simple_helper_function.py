#!/usr/bin/env python3
"""
Simple Helper Function Module
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: Tuple containing start index and end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end

#!/usr/bin/env python3
"""There are no modules to be imported."""


def index_range(page, page_size):
    """Return a tuple that contains first and last indices of a page."""

    first = (page - 1) * page_size
    last = (page * page_size)
    return (first, last)

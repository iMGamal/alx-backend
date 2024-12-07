#!/usr/bin/env python3
def index_range(page, page_size):
    first = (page - 1) * page_size
    last = (page * page_size)
    return (first, last)

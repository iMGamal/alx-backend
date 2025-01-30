#!/usr/bin/env python3
"""These are the modules for our program."""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Class constructor."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the requested page."""
        if page and page_size:
            assert isinstance(page, int), "page should be an integer"
            assert page > 0, "page should be more than 0"
            assert isinstance(page_size, int), "page_size should be an integer"
            assert page_size > 0, "page_size should be more than 0"

        return self.__dataset

get_page(3.45, 12)

#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination"""
        datakey = self.indexed_dataset()
        assert isinstance(index, int) and index < len(datakey)
        assert isinstance(page_size, int) and page_size > 0

        data_len = len(datakey)
        current = index if index in datakey else next(
            i for i in range(index, data_len) if i in datakey
        )

        return {
            "index": index,
            "data": [
                datakey[i]
                for i in range(current, current + page_size) if i in datakey
            ],
            "page_size": page_size,
            "next_index": current + page_size
        }

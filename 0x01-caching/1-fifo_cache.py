#!/usr/bin/env python3
""" FIFO Cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
        Implements a FIFO caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.cache_order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.cache_order.pop(0)
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

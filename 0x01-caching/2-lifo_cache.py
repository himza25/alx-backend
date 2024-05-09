#!/usr/bin/env python3
""" LIFO Cache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
        Implements a LIFO caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.last_key
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

        self.last_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

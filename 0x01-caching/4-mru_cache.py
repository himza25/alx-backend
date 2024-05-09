#!/usr/bin/env python3
""" MRU Cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
        Implements an MRU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.last_key
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")
            self.last_key = next(reversed(self.cache_data), None)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        self.last_key = key
        return self.cache_data[key]

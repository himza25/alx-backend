#!/usr/bin/env python3
""" MRU Caching Module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class, inheriting from BaseCaching and implementing
    the MRU caching system.
    """
    def __init__(self):
        """ Initialize the MRUCache class
        """
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """ Add an item to the cache using MRU policy
        """
        if key is None or item is None:
            return

        # If key already exists, update value and move to most recent position
        if key in self.cache_data:
            self.cache_data[key] = item
            self.mru_keys.remove(key)
            self.mru_keys.append(key)
        else:
            # If cache is full, discard most recently used
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.mru_keys.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            # Add new item
            self.cache_data[key] = item
            self.mru_keys.append(key)

    def get(self, key):
        """ Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        # Move key to the most recent position
        self.mru_keys.remove(key)
        self.mru_keys.append(key)
        return self.cache_data[key]

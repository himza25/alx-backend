#!/usr/bin/env python3
""" LFU Caching Module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and implements
    the LFU caching system.
    """

    def __init__(self):
        """ Initialize the LFUCache class
        """
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """ Add an item to the cache using LFU policy
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = min(self.frequency.values())
                least_freq_keys = [
                    k for k, freq in self.frequency.items()
                    if freq == least_freq
                ]

                if len(least_freq_keys) > 1:
                    to_discard = next(
                        k for k in self.usage_order if k in least_freq_keys
                    )
                else:
                    to_discard = least_freq_keys[0]

                del self.cache_data[to_discard]
                del self.frequency[to_discard]
                self.usage_order.remove(to_discard)
                print(f"DISCARD: {to_discard}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]

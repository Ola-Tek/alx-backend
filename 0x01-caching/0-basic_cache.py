#!/usr/bin/env python3
"""Script for a basic module cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """it represent an object that allows storing and
    retrieving objects from a temporary memory like a dictionary.
    """
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)

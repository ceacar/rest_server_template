import sys
from typing import TypeVar
import errors

T = TypeVar('T')

class Cacher:
    """
    use a cacher to cache key value pair store
    """

    def __init__(self):
        self.internal_cache = {}

    def save(self, key: str, value: T):
        self.internal_cache[key] = value

    def delete(self, key: str):
        retrieved_value = self.internal_cache.get(key, None)
        if retrieved_value:
            del self.internal_cache[key]
        else:
            raise errors.InvalidKey("attmpting to delete non exist value with key {0}".format(key))

    def get(self, key: str) -> T:
        return self.internal_cache.get(key, None)

__cacher = None

def get_cacher():
    #singleton
    global __cacher

    if not __cacher:
        __cacher = Cacher()

    return __cacher

import sys
from typing import TypeVar

T = TypeVar('T')

class Cacher:

    def __init__(self):
        self.internal_cache = {}

    def save(self, key: str, value: T,
             ):
        self.internal_cache[key] = value

    def delete(self, key: str):
        retrieved_value = self.internal_cache.get(key, None)
        if retrieved_value:
            del self.internal_cache[retrieved_value]
        else:
            raise Exception("attmpting to delet non exist key")

    def get(self, key: str) -> T:
        return self.internal_cache.get(key, None)

__cacher = None

def get_cacher():
    #singleton
    global __cacher

    if not __cacher:
        __cacher = Cacher()

    return __cacher

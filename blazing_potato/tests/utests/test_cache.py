import unittest
import cache
import errors

class TestClassExample(unittest.TestCase):
    def setUp(self):
        self.cacher = cache.get_cacher()
        self.cacher.internal_cache = {}

    def test_save(self):
        self.cacher.save("key1","value1")
        assert self.cacher.internal_cache == {"key1":"value1"}

    def test_get(self):
        self.cacher.save("key2","value2")
        assert self.cacher.get("key2") == "value2"

    def test_delete(self):
        self.cacher.save("key2","value2")
        self.cacher.delete("key2")
        assert self.cacher.internal_cache == {}

        try:
            self.cacher.delete("key3")
            assert False
        except errors.InvalidKey:
            assert True

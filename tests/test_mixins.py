import unittest
from devmap import mixins
from nose_parameterized import parameterized, param


class BitOpsMixinTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mixin = mixins.BitOpsMixin()

    @parameterized.expand([
        # Set bits
        param(0, 0, 1, 1),
        param(0, 1, 1, 2),
        param(1, 1, 1, 3),
        param(5, 1, 1, 7),
        param(4, 2, 1, 4),

        # Clear bits
        param(4, 2, 0, 0),
        param(5, 1, 0, 5),
        param(7, 1, 0, 5),
    ])
    def test_set_bit(self, val, bit, set, expected):
        self.assertEqual(self.mixin.set_bit(val, bit, set), expected)

    @parameterized.expand([
        param(10, 1, 1024),
        param(32, 1, 4294967296),
        param(10, 2, 2048),
        param(0, 1024, 1024)
    ])
    def test_lshift(self, n, val, expected):
        self.assertEqual(self.mixin.lshift(n, val), expected)

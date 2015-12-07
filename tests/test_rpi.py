import struct
import unittest
from io import BytesIO
from devmap.rpi.gpio import GPIO


class TestRPi(unittest.TestCase):
    def test_base_address_parsing(self):
        data = struct.pack('>II', 0, 0xffb)
        bio = BytesIO(data)
        base_addr = GPIO._find_base_address(bio)
        self.assertEqual(base_addr, 0xffb)

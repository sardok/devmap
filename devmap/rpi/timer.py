from zope.interface import implements
from devmap.interfaces import ISysTimer
from devmap.mixins import BitOpsMixin

from devmap.rpi.base import RPiMemMapBase
from devmap.rpi.register_maps import BCM2835_REGISTER_MAP


class SysTimer(RPiMemMapBase, BitOpsMixin):
    implements(ISysTimer)

    def __init__(self, register_map=None):
        self.register_map = register_map or BCM2835_REGISTER_MAP
        address, length = self._find_address_and_length(
            self.register_map, 'SYS_TIMER_BASE', 'SYS_TIMER_LEN')
        self._mm = self._initialize_mmap(address, length)

    def value(self):
        lo_addr = self._get_register_offset(self.register_map, 'sys_timer_clo')
        hi_addr = self._get_register_offset(self.register_map, 'sys_timer_chi')

        lo_val = self._get_register_value(self._mm, lo_addr)
        hi_val = self._get_register_value(self._mm, hi_addr)

        return (hi_val << 32) | lo_val

    def reset(self):
        addr = self._get_register_offset(self.register_map, 'sys_timer_cs')
        self._set_register_value(self._mm, addr, 0)

import os
import struct
import mmap
from devmap.exceptions import UnsupportedSystem


class RPiMemMapBase(object):

    @staticmethod
    def _initialize_mmap(offset, length):
        fd = os.open('/dev/mem', os.O_RDWR | os.O_SYNC)
        return mmap.mmap(fd, length, offset=offset)

    @staticmethod
    def _find_base_address(fio=None):
        try:
            fio = fio or open('/proc/device-tree/soc/ranges')
            with fio:
                fio.seek(4)
                sz = struct.calcsize('I')
                addr_raw = fio.read(sz)
                base, = struct.unpack('>I', addr_raw)
                return base
        except (IOError, struct.error):
            pass

    def _find_address_and_length(self, register_map, base_key, length_key):
        try:
            base_address = self._find_base_address() or \
                           register_map['PERI_VIRT_BASE']
            address = base_address + register_map[base_key]
            length = register_map[length_key]
            return address, length
        except IndexError:
            raise UnsupportedSystem(
                'Unable to determine peripheral or system timer base address')

    @staticmethod
    def _get_register_offset(register_map, key, default=None):
        return register_map.get(key.upper(), default)

    @staticmethod
    def _get_register_value(buffer, addr):
        reg_val, = struct.unpack_from('=I', buffer, addr)
        return reg_val

    @staticmethod
    def _set_register_value(buffer, addr, value):
        struct.pack_into('=I', buffer, addr, value)

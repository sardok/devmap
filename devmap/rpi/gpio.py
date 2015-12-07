from zope.interface import implements
from devmap.exceptions import InvalidArgument
from devmap.interfaces import IGPIO
from devmap.mixins import BitOpsMixin
from devmap.rpi.register_maps import BCM2835_REGISTER_MAP
from devmap.rpi.base import RPiMemMapBase


class GPIO(RPiMemMapBase, BitOpsMixin):
    implements(IGPIO)

    def __init__(self, gpio_no, direction='in', initial=None, edge='both',
                 register_map=None):
        self.register_map = register_map or BCM2835_REGISTER_MAP

        address, length = self._find_address_and_length(
            self.register_map, 'GPIO_BASE', 'GPIO_LEN')
        self._mm = self._initialize_mmap(address, length)
        self.gpio_no = gpio_no
        self.set_edge_mode(edge)
        self.set_direction(direction)
        self.clear()
        if initial is not None:
            self.write(initial)

    def clear(self):
        val = self.lshift(self.gpio_no % 32)
        addr = self._get_register_offset(self.register_map, 'gpio_gpclr0')
        self._set_register_value(self._mm, addr, val)

    def write(self, value):
        enabled = 1 if value else 0
        self.clear()
        addr = self._get_register_offset(self.register_map, 'gpio_gpfset0')
        val = self._get_register_value(self._mm, addr)
        nval = self.set_bit(val, self.gpio_no, enabled)
        self._set_register_value(self._mm, addr, nval)

    def read(self):
        addr = self._get_register_offset(self.register_map, 'gpio_gplev0')
        reg_val = self._get_register_value(self._mm, addr)
        return 1 if reg_val & self.lshift(self.gpio_no) else 0

    def set_high_detect(self, enable):
        address = self._get_register_offset(self.register_map, 'gpio_gphen0')
        reg_val = self._get_register_value(self._mm, address)
        if enable:
            return reg_val | self.lshift(self.gpio_no)
        else:
            return reg_val & self.lshift_and_negate(self.gpio_no)

    def set_edge_mode(self, mode):
        modes = {'falling': ['gpio_gpfen0'], 'raising': ['gpio_gpren0'],
                 'both': ['gpio_gpfen0', 'gpio_gpren0'], 'none': []}
        mode = mode.lower()
        if mode not in modes:
            raise InvalidArgument('Invalid edge mode {} (supported modes {})'
                                  .format(mode, ', '.join(modes.keys())))
        registers = modes[mode]
        for register in registers:
            addr = self._get_register_offset(self.register_map, register)
            val = self._get_register_value(self._mm, addr)
            modified = self.set_bit(val, self.gpio_no, 1)
            self._set_register_value(self._mm, addr, modified)

    def _gpio_setup_out(self, gpio, reg_val):
        reg_val |= self.lshift((gpio % 10) * 3)
        return reg_val

    def _gpio_setup_in(self, gpio, reg_val):
        reg_val &= self.lshift_and_negate((gpio % 10) * 3, 7)
        return reg_val

    def set_direction(self, direction):
        directions = {'in': self._gpio_setup_in, 'out': self._gpio_setup_out}
        direction = direction.lower()
        if direction not in directions:
            raise InvalidArgument(
                ('Invalid direction {}, supported directions are in and out.'
                 .format(direction)))
        cb = directions[direction]
        offset = self.gpio_no // 10
        register = 'gpio_gpfsel{}'.format(offset)
        addr = self._get_register_offset(self.register_map, register)
        val = self._get_register_value(self._mm, addr)
        nval = cb(self.gpio_no, val)
        self._set_register_value(self._mm, addr, nval)

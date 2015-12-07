class BitOpsMixin(object):
    @staticmethod
    def set_bit(value, bit, set):
        if set:
            return value | (1 << bit)
        else:
            return value & ~(1 << bit)

    @staticmethod
    def lshift(n, val=1):
        return val << n

    def lshift_and_negate(self, n, val=1):
        return ~self.lshift(n, val)

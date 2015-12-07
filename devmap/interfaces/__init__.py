from zope.interface import Interface


class IGPIO(Interface):
    def read(self):
        """
        Reads value of configured GPIO pin.
        :return: 1 or 0
        """

    def write(self, value):
        """
        Writes give value to configured GPIO pin as 1 or 0.
        """

    def clear(self):
        """
        Clears configured GPIO pin.
        """

    def set_direction(self, direction):
        """
        Set configured GPIO pin direction
        :param direction: 'in' or 'out'
        """


class ISysTimer(Interface):
    def value(self):
        """ Returns current value of timer """

    def reset(self):
        """ Reset the timer """

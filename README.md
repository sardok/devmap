# devmap
SoC peripheral library.

## Keynotes ##

This library maps `/dev/mem` and uses memory region associated to the peripheral.

The mapping is done by [mmap](https://docs.python.org/2/library/mmap.html) function from standard library.

Implementation is in pure python.

## Supported peripherals ##

* GPIO
* System timer

## Supported platforms ##

* Raspberry Pi 2

## Examples ##

#### GPIO ####

```python
from devmap.rpi.gpio import GPIO

# Read input from GPIO 21
gio_21 = GPIO(21, 'in')
gio_21.read()

# Write to particular pin
gio_out = GPIO(2, 'out')

gio_out.write(1)
gio_out.read() # 1

gio_out.write(0)
gio_out.read() # 0
```

#### System timer ####

```python

from devmap.rpi.timer import SysTimer

st = SysTimer()

st.value()  # 507968675
st.value()  # 508968736
```

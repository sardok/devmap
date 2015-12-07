# https://www.raspberrypi.org/wp-content/uploads/2012/02/BCM2835-ARM-Peripherals.pdf
BCM2835_REGISTER_MAP = {
    'PERI_VIRT_BASE': 0x20000000,

    # GPIO offsets
    'GPIO_BASE': 0x200000,
    'GPIO_LEN': 0x100,
    'GPIO_GPFSEL0': 0x0,
    'GPIO_GPFSEL1': 0x4,
    'GPIO_GPFSEL2': 0x8,
    'GPIO_GPFSEL3': 0xc,
    'GPIO_GPFSEL4': 0x10,
    'GPIO_GPFSEL5': 0x14,
    'GPIO_GPFSET0': 0x1c,
    'GPIO_GPFSET1': 0x20,
    'GPIO_GPCLR0': 0x28,
    'GPIO_GPCLR1': 0x2c,
    'GPIO_GPLEV0': 0x34,
    'GPIO_GPLEV1': 0x38,
    'GPIO_GPEDS0': 0x40,
    'GPIO_GPEDS1': 0x44,
    'GPIO_GPREN0': 0x4c,
    'GPIO_GPREN1': 0x50,
    'GPIO_GPFEN0': 0x58,
    'GPIO_GPFEN1': 0x5c,
    'GPIO_GPHEN0': 0x64,
    'GPIO_GPHEN1': 0x68,

    # System Timer offsets
    'SYS_TIMER_BASE': 0x3000,

    # sys timer len is heuristic value
    'SYS_TIMER_LEN': 0x68,
    'SYS_TIMER_CS': 0x0,
    'SYS_TIMER_CLO': 0x4,
    'SYS_TIMER_CHI': 0x8,
    'SYS_TIMER_C0': 0xc,
    'SYS_TIMER_C1': 0x10,
    'SYS_TIMER_C2': 0x14,
    'SYS_TIMER_C3': 0x18,
}

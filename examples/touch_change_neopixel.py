# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 Seth Kerr for Oak Development Technologies
#
# SPDX-License-Identifier: Unlicense

"""
Example showing how to use the AT42QT1070 touch sensor!
"""

import board
import busio
import time  # pylint: disable=C0411
import odt-at42qt1070-python
import neopixel  # pylint: disable=C0411

num_pixels = 1  # pylint: disable=C0103

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=0.3, auto_write=False)

i2c = busio.I2C(board.SCL, board.SDA)

qtouch = odt-at42qt1070-python.AT42QT1070(i2c)

while True:
    if qtouch.touched():
        pixels.fill(GREEN)
        pixels.show()
        time.sleep(1)
    else:
        pixels.fill(RED)
        pixels.show()
        time.sleep(1)

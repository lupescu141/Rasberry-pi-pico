import ssd1306
import fifo
import time
from machine import Pin, I2C
import ssd1306

import micropython
micropython.alloc_emergency_exception_buf(200)


rb = fifo.Fifo(50)
print('I am test.py')

if rb.empty():
    print('Fifo is empty')

led = Pin("LED", Pin.OUT)

# using default address 0x3C
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

class ufo():
    
    def __init__(self):
        
    def move_left(self):

while True:
    


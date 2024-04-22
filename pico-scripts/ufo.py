import fifo
import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

import micropython
micropython.alloc_emergency_exception_buf(200)

sw0 = Pin(9, Pin.IN, Pin.PULL_UP)
sw2 = Pin(7, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)


print('I am test.py')



class UFO():
    
    def __init__(self):
        
        self.locationX = 57
        self.locationY = 57
        self.shipBody = "<=>"
        self.locationMax = 104
        self.locationMin = 0
        
    def spawn_ufo(self):
        oled.fill(0)
        oled.text('<=>', self.locationX, self.locationY, 1)
        oled.show()
        
    def move_left(self):
        
        self.locationX -=1
        
    def move_right(self):
        
        self.locationX +=1
        

ufo = UFO()
ufo.spawn_ufo()

while True:
    time.sleep(0.01)
    print(sw0())

    if sw2() == 0 and ufo.locationX > ufo.locationMin:
        ufo.move_left()
        ufo.spawn_ufo()
        
    if sw0() == 0 and ufo.locationX < ufo.locationMax:
        ufo.move_right()
        ufo.spawn_ufo()
    
    
import fifo
import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
import micropython
micropython.alloc_emergency_exception_buf(200)


sw0 = Pin(9, Pin.IN, Pin.PULL_UP)
sw1 = Pin(8, Pin.IN, Pin.PULL_UP)
sw2 = Pin(7, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)


class Line():
    
    def __init__(self):
        
        self.locationX = 0
        self.locationY = 32
        self.locationXmax = 128
        self.locationXmin = 0
        self.locationYmax = 0
        self.locationYmin = 63
        
        
    def reset_line(self):
        
        oled.fill(0)
        self.locationX = 0
        self.locationY = 32
        oled.pixel(self.locationX,self.locationY,1)
        oled.show()
        
        
    def move_up(self):
        
        self.locationY -= 1
        
        
    def move_down(self):
        
        self.locationY += 1
        
        
    def move_line(self):
        
        if self.locationX > self.locationXmax:
            
            self.locationX = 0
        
        else:
            
            self.locationX += 1
            
        oled.pixel(self.locationX,self.locationY,1)
        oled.show()

line = Line()
line.reset_line()

while True:
    
    time.sleep(0.01)

    if sw2() == 0 and line.locationY > line.locationYmax:
        
        line.move_up()
        
    if sw1() == 0:
        
        line.reset_line()
        
    if sw0() == 0 and line.locationY < line.locationYmin:
        
        line.move_down()
    
    line.move_line()
    
    

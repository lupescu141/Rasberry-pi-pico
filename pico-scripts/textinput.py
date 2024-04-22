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


class Textbox():
    
    def __init__(self):
         
         self.textList = []
         self.yValue = 0
         
    def printText(self):
         
        self.yValue = 0
        oled.fill(0)
         
        if len(self.textList) == 8:
             
            self.textList.pop(0)
        
        self.textList.append(input())
        
        for textLine in self.textList:
            
            oled.text(textLine, 0, self.yValue, 1)
            self.yValue += 8
        
        oled.show()

textBox = Textbox()
            
while True:
    
    time.sleep(0.05)
    textBox.printText()
    
   
    
    
    
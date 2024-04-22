from filefifo import Filefifo
import time
import micropython
micropython.alloc_emergency_exception_buf(200)
    
class Fifo():
    
    def __init__(self, sampleTxtFileName, sampleRange):
        
        self.data = Filefifo(10, name = sampleTxtFileName)
        self.sampleList = []
        self.sampleRange = sampleRange
    
    def printRangeData(self, minRange, maxRange):
        
        for i in range(self.sampleRange):
    
            self.sampleList.append(self.data.get())
    
        for i in self.sampleList:
            
            print(f"{(i - min(self.sampleList)) / (max(self.sampleList) - min(self.sampleList)) * (maxRange - minRange) :.0f}")
   

fifo = Fifo('capture_250Hz_01.txt', 2500)
fifo.printRangeData(0, 100)
    

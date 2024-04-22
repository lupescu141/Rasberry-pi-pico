from filefifo import Filefifo
import time
import micropython
micropython.alloc_emergency_exception_buf(200)
    
class Fifo():
    
    def __init__(self, sampleTxtFileName, sampleRange):
        
        self.data = Filefifo(10, name = sampleTxtFileName)
        self.sampleList = []
        self.sampleRange = sampleRange
        self.samplesBetweenPeaks = []
        self.peaked = False
        self.peakList = []
        self.bottomList = []
        self.sampleCount = 0
    
    
    def printPeakData(self):
        
        for i in range(self.sampleRange):
    
            self.sampleList.append(self.data.get())
            self.sampleCount += 1
    
            if self.sampleList[i] < self.sampleList[i - 1] and i > 0 and self.peaked == False:
        
                print(self.sampleList[i - 1])
                self.peakList.append(self.sampleList[i - 1])
                self.samplesBetweenPeaks.append(self.sampleCount)
                self.sampleCount = 0
                self.peaked = True
        
            if self.sampleList[i] > self.sampleList[i - 1] and i > 0 and self.peaked == True:
                
                print(self.sampleList[i - 1])
                self.peaked = False
                self.bottomList.append(self.sampleList[i - 1])
                
        for i in range(len(self.peakList)):
            
            if i == 0:
                continue 
            
            try:
            
                print(f'Peak interval {i}:\n'
                      + f'   Peak: {self.peakList[i]}\n'
                      + f'   Bottom: {self.bottomList[i]}\n'
                      + f'   Peak: {self.peakList[i + 1]}\n'
                      + f'   Samples in between: {self.samplesBetweenPeaks[i]}\n'
                      + f'   Seconds in between: {self.samplesBetweenPeaks[i] / 250}\n'
                      + f'   Frequency: {1 / (self.samplesBetweenPeaks[i] / 250)}\n\n')
                
            except:
                
                return 
   

fifo = Fifo('capture_250Hz_01.txt', 2500)
fifo.printPeakData()
    

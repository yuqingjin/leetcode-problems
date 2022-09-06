# Method: heapq, T: O(logN)
# use two heapq to maintain numbers > median and <= median
from heapq import *
class MedianFinder:
    def __init__(self):
        # store as a max heap
        self.queMin = list()
        self.queMax = list()
    
    def addNum(self, num: int) -> None:
        if not self.queMin:
            heappush(self.queMin, -num)
            return
        
        median = -self.queMin[0]
        if len(self.queMin) > len(self.queMax):
            if num > median:
                heappush(self.queMax, num)
            else:
                heappush(self.queMin, -num)
                heappush(self.queMax, -heappop(self.queMin))
        
        else:
            if num > median:
                heappush(self.queMax, num)
                heappush(self.queMin, -heappop(self.queMax))
            else:
                heappush(self.queMin, -num)
            
    def findMedian(self) -> float:
        if len(self.queMin) > len(self.queMax):
            median = -self.queMin[0]
        else:
            median = (-self.queMin[0] + self.queMax[0]) / 2
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

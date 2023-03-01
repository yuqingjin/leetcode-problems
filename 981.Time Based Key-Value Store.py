'''
1. look for the most right timestamp --> bisect_right --> find[idx-1]
2. format: arr.bisect_right(value)

# Method: Binary Search
# Time Complexity: O(logN);
# Space Complexity: O(N)
'''

from sortedcontainers import SortedDict, SortedList
from bisect import *
class TimeMap:
    def __init__(self):
        self.dict = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if self.dict[key] == {}:
            return ""
        
        idx = self.dict[key].bisect_right(timestamp)
        if idx == 0:
            return ""
        else:
            return self.dict[key].peekitem(idx-1)[1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

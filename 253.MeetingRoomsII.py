# Method: heapq
# T: O(NlogN)
# S: O(N)

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key = lambda x:x[0])
        # print(intervals)
        heap = []
        room = 0
        
        for i, time in enumerate(intervals):
            start, end = time[0], time[1]

            while heap and heap[0] <= time[0]:
                heapq.heappop(heap)
                
            heapq.heappush(heap, time[1])
            room = max(room, len(heap))
        
        return room

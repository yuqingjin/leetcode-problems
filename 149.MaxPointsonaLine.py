# Method: enumerate + hashtable
# T: O(N^2)
# S: O(N)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        # (slope, b) as key, indexes as values
        hashtable = defaultdict(set) # store points on the same line
        
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points):
                
                if point1 != point2:
                    # slope doesnt exist
                    if point2[0]-point1[0] == 0:
                        slope = None
                        b = point2[0] # intersection of line and x-axis
                    else:
                        slope = (point2[1]-point1[1]) / (point2[0]-point1[0])
                        b = point2[1] - (point2[0] * slope) # intersection of line and y-axis
                    hashtable[(slope, b)].add(i)
                    hashtable[(slope, b)].add(j)
                    res = max(res, len(hashtable[(slope, b)]))
                    
        return res

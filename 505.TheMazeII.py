# Method: DFS + BFS(heapqueue)
# basic idea: dfs for travesing all the end points from a start point; bfs and heapq for poping the current smallest dist out and keep tracking it following DFS rule
# T: O(mn)
# S: O(mn)
# ref: https://zhenyu0519.github.io/2020/03/22/lc505/#codedfsbfs

from heapq import *
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        start, destination = tuple(start), tuple(destination)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(node):
            temp = []
            # 新建used set, 防止同一个node能到达的位置重复
            used = set()
            used.add(node)
            
            for dx, dy in directions:
                (x, y), dist = node, 0
                while x+dx in range(m) and y+dy in range(n) and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    dist += 1
                
                if (x, y) not in used:
                    temp.append((dist, (x, y)))
                    
            return temp
        
        # 新建visited set, 防止重复遍历
        visited = set()
        # heapqueue, 为了能先将当前dist最小的pop出来
        heap = [(0, start)]
        while heap:
            dist, position = heappop(heap)
            if position in visited:
                continue
            visited.add(position)
            if position == destination:
                return dist
            
            for neigh_dist, neigh_position in dfs(position):
                heappush(heap, (dist + neigh_dist, neigh_position))
        
        return -1

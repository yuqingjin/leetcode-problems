# Method: Topo sort + BFS(in-degree)
# T: O(V+E); V-num of vertex, E-num of edge
# S: O(V+E)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        post = defaultdict(list)
        res = []
        visited = set()
        
        for p in prerequisites:
            a, b = p[0], p[1]
            post[b].append(a)
            indegree[a] += 1
            
        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                visited.add(i)
        
        while q:
            length = len(q)
            for i in range(length):
                cur = q.pop(0)
                res.append(cur)
                for c in post[cur]:
                    indegree[c] -= 1
                    if indegree[c]==0 and c not in visited:
                        q.append(c)
        
        # if cannot finish all the courses return empty array
        if len(res) != numCourses:
            return []
        
        return res

# Method: Topological sort + BFS(indegree)
# T: O(V+E), V-num of vertexs, E-num of edges
# S: O(V+E)
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        post = defaultdict(list)
        course = 0
        
        for p in prerequisites:
            a, b = p[0], p[1]
            indegree[a] += 1
            post[b].append(a)
        
        # Topological order + BFS 
        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # print(q)
        while q:
            leng = len(q)
            for i in range(leng):
                cur = q.pop(0)
                course += 1

                for c in post[cur]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        q.append(c)

        return course == numCourses

        

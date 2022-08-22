# Method: unionfind
# basic idea: 构造n叉树，以某一个除数为root，将它的被除数作为子节点；不断并查；每个点的value为它到根节点的倍数差
# T: O((N+M)*logN); N-length of input, M-length of output, NlogN-time complexity of unionfind for input
# S: O(N)

class unionfind:
    def __init__(self):
        self.parent = {}
        self.value = {}
        
    def find(self, x):
        root = x
        base = 1
        
        while self.parent[root] != root:
            root = self.parent[root]
            base *= self.value[root]
            
        while x != root:
            original_parent = self.parent[x]
            self.value[x] *= base
            base /= self.value[original_parent]
            
            self.parent[x] = root
            x = original_parent
        
        return root
    
    
    def connect(self, x, y):
        p_x, p_y = self.find(x), self.find(y)
        return p_x == p_y
        
    def merge(self, x, y, value):
        p_x, p_y = self.find(x), self.find(y)
        # 如果相等，通过find之后，二者的value应该已经存在
        if p_x != p_y:
            self.parent[p_x] = p_y
            self.value[p_x] = (self.value[y] * value) / self.value[x]
            
    
    def add(self, x):
        # 这里不要忘记
        if x not in self.parent:
            self.parent[x] = x
            self.value [x] = 1.0
    
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = unionfind()
        for [a, b], value in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, value)
        
        res = []
        for [c, d] in queries:
            if c in uf.parent and d in uf.parent and uf.connect(c, d):
                res.append(uf.value[c] / uf.value[d])  
            else:
                res.append(-1.0)
        return res
        

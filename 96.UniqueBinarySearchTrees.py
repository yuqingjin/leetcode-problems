'''
Method: dp, using the previous computed configuration num
T: O(N^2)
S: O(N)
ref: https://leetcode.com/problems/unique-binary-search-trees/solutions/2645217/python-solution/?orderBy=hot&languageTags=python
'''
class Solution:
    def numTrees(self, n: int) -> int:
        cache = [0] * (n+1) 
        cache[0], cache[1] = 1, 1 # for cache[0] == 1 and cache[1] == 1

        # the current node being computed
        for cur_node in range(2, n+1):
            # regarding which node as the root_node
            for root_node in range(1, cur_node+1):
                # left-side and right-side nodes configuration
                left = cur_node - root_node 
                right = root_node - 1
                cache[cur_node] += cache[left] * cache[right]

        return cache[-1]

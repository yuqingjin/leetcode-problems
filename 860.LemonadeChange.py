# Method: greedy
# T: O(N) 
# S: O(1) 

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                hashmap[5] += 1
                
            elif bill == 10:
                if hashmap[5] >= 1:
                    hashmap[10] += 1
                    hashmap[5] -= 1
                else:
                    return False
                
            else:
                if hashmap[10] and hashmap[5]:
                    hashmap[20] += 1
                    hashmap[10] -= 1
                    hashmap[5] -= 1
                
                elif hashmap[5] >= 3:
                    hashmap[20] += 1
                    hashmap [5] -= 3
                    
                else:
                    return False
        return True

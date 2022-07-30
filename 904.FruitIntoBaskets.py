# Method: Sliding window + hashmap
# Time: O(N); n - length of fruits
# Space: O(N)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        begin = end = 0
        basket = defaultdict(int)
        max_fruit = 0
        
        # end pointer sliding to the right
        while end < len(fruits):
            # store the frequency of each type of fruit in dict
            basket[fruits[end]] +=1
            
            # when num of type go over the maximum type num
            while len(basket) > 2:
                # update max_fruit based on the previous situation
                max_fruit = max(max_fruit, end-begin)
                
                # 方法1 窗口右端左滑：
                # 从end-1开始向左滑动窗口，直到出现篮子里未出现的水果type
                # 删去dict中该水果type的key
                begin = end-1
                while fruits[begin]==fruits[begin-1]:
                    begin-=1
                del basket[fruits[begin-1]]
                
                # 方法2 窗口左端右滑：
                # 从end-1开始向左滑动窗口，直到出现篮子里未出现的水果type
                # 删去dict中该水果type的key
                # basket[fruits[begin]] -=1
                # if basket[fruits[begin]] == 0:
                #     del basket[fruits[begin]]
                # begin += 1
                
            end += 1
            
        return max(max_fruit, end-begin)
                

# method: custom comparator, T: O(N)

# inheritance from str
class largerNumKey(str):
    # overloading lt method
    # 不加self, 是为了从外部call this method
    def __lt__(x:str, y:str):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            
        res = sorted(map(str, nums), key=largerNumKey)
        return "".join(res) if res[0] != "0" else "0"

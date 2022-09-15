# method: binary search
# basic idea: keep tracking of the relation between leftmost val and rightmost val; comparing mid_val with them to decide the next tracking range
# T: O(logN)
# S: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        res = nums[0]
        
        while l <= r:
            # 左等于右，说明可以range length为1；return res
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res    
            
            mid = (l+r) // 2
            if nums[l] <= nums[mid]:
                # 不断更新最小，防止出现mid==l, 没更新最小的情况出现
                res = min(res, nums[l])
                l = mid + 1
            
            else:
                res = min(res, nums[mid])
                r = mid - 1
                
        return res

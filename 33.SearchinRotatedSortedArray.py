# method: binary search, in a partial sorted array
# Basic idea: find the sorted portion, target either in range[nums[l], nums[r]] of this portion or in the other one
# T: O(logN)
# S: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l + r) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            
            # check left and right portion
            # first, assume left portion is sorted:
            if nums[l] <= mid_val:
                if target < mid_val and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # when right portion is sorted
            else:
                if target > mid_val and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1

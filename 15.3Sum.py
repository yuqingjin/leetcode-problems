# Method: two pointers
# Basic idea: continued with the method using in TwoSum II, we still use Two-Pointer method to solve this pro. To avoid the duplicate, 1. we use i+1 as the start of our left pointer; 2.we use while loop to update the num left pointer pointing to.
# Time: O(N^2) + O(NlogN) = O(N^2); need one traversal and a nested traversal
# Space: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            
            if i > 0 and num == nums[i-1]:
                continue
                
            l, r = i+1, len(nums)-1
            
            while l < r:
                total = num + nums[l] + nums [r]
                if total < 0:
                    l += 1
                        
                elif total > 0:
                    r -= 1
                    
                else:
                    res.append([num, nums[l], nums[r]])
                    
                    # e.g.[-2,-2,0,0,2,2]
                    
                    # Method 1: shifting both left and right pointers 
                    # l+=1
                    # r-=1
                    # while l < r and nums[l] == nums[l-1]:
                    #     l+=1
                    # while l < r and nums[r] == nums[r+1]:
                    #     r-=1
                        
                    # Method 2: Or just shifting the left pointer, and got same result
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    
        return res 

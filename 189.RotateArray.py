class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # method3: reverse the array
        k %= len(nums)
        def reverse(arr):
            l, r = 0, len(arr)-1
            while l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            return arr
        
        nums = reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])
        
        # T:O(N), S:O(1)
        # use start variable to avoid the cycle
#         start = count = 0
#         n = len(nums)
#         k %= n
        
#         while count < n:
#             current_idx, prev_val = start, nums[start]
#             while True:
#                 next_idx = (current_idx + k) % n
#                 nums[next_idx], prev_val = prev_val, nums[next_idx]
#                 current_idx = next_idx
#                 count += 1
#                 print("start", start)
#                 print("current_idx", current_idx)
#                 if start == current_idx:
#                     break
            
#             start += 1

        
#         n = len(nums)
#         nums_copy = [0] * n
#         k %= n
        
#         for i, num in enumerate(nums):
#             if i + k < n:
#                 nums_copy[i+k] = num
            
#             else:
#                 nums_copy[i+k-n] = num
                
#         for i, num in enumerate(nums_copy):
#             nums[i] = nums_copy[i]
        
        

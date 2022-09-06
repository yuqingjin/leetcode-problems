from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        # Method: mergesort; T: O(NlogN), S:O(1)
        # ref: https://leetcode.cn/problems/count-of-smaller-numbers-after-self/solution/4chong-jie-fa-yi-wang-da-jin-pai-xu-shu-5vvds/
        # can sort and find the num smaller than the current from the merged list
        res = []
        def mergeSort(nums, low, high):
            if low >= high:
                return 0
            
            mid = (high+low) // 2
            mergeSort(nums, low, mid)
            mergeSort(nums, mid+1, high)
            
            # now, we have sorted left array and right array
            temp = []
            left, right = low, mid+1
            
            # end case: one array run out of elements
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    # record the num of elements smaller than current in right array
                    res[nums[left][1]] += right - (mid+1)
                    left += 1
        
                else:
                    temp.append(nums[right])
                    # for right element, we dont need to update the num, since we only need smaller numbers after self
                    # res[nums[right][1]] += mid - left
                    right += 1
            
            # process another array that still have elements
            while left <= mid:
                temp.append(nums[left])
                # num of elements smaller than current in right array
                res[nums[left][1]] += right - (mid+1)
                left += 1
            while right <= high:
                temp.append(nums[right])
                # res[nums[right][1]] += mid - left
                right += 1
                
            nums[low:high+1] = temp
        
        res = [0] * len(nums)
        # to store the index for return output
        nums = [(num, index) for index, num in enumerate(nums)]
        mergeSort(nums, 0, len(nums)-1)
        return res
        
#         Method: sortedList + binary select
#         T: O(NlogN); bisect: T(logN)
        # lst = SortedList()
        # res = [0] * len(nums)
        # for i in range(len(nums)-1, -1, -1):
        #     lst.add(nums[i])
        #     idx = lst.bisect_left(nums[i])
        #     res[i] = idx
        # return res
            
        
#       Method: brute force; T: O(N^2), TLE
        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] > nums[j]:
        #             res[i] += 1
        # return res
            

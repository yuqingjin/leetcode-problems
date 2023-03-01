'''
1. no duplicate quadruplets
2. avoid nums[i] == nums[i+1], nums[j] == nums[j+1] ...
Time Complexity: O(N^2*log(N))
Space Complexity: Comb(N, 4)
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                l, r = j+1, len(nums)-1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        if (nums[i], nums[j], nums[l], nums[r]) in res:
                            l += 1
                            continue
                        else:
                            res.add((nums[i], nums[j], nums[l], nums[r]))
                            l += 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1

        return list(list(x) for x in res)

# Method: Three pointers, starting from the end 
# T: O(n+m)
# S: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = len(nums1) -1
        
        # 从后往前放置
        while j >= 0 and i <= k and i >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        
        # 上述如果nums1队列原数被填完了，但nums2队列还没被填完，
        # 这里while loop继续填充
        while j >= 0 and k >=0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

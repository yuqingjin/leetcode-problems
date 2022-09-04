class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         Method 2: compute product from leftmost to current and from rightmost to current(exclusively)
        length = len(nums)
        answers = [0] * length
        
        # compute the product from leftmost to the current(exclusively), so initialize index 0 to 1
        answers[0] = 1
        for i in range(1, length):
            answers[i] = answers[i-1] * nums[i-1]
        
#         compute the product from right most to the current(exclusively)
        R = 1
        for i in range(length-1, -1, -1):
            answers[i] *= R
            R *= nums[i]
            
        return answers

        
#         Method 1: T:O(N); S:O(1)
#         product = 1
#         zeros = 0
#         answers = []
        
#         for num in nums:
#             if num == 0:
#                 zeros += 1
#                 continue
#             product *= num
            
#         for num in nums:
#             if num != 0:
#                 if zeros > 0:
#                     answers.append(0)
#                 else:
#                     answers.append(product//num)

#             else:
#                 if zeros == 1:
#                     answers.append(product)
#                 else:
#                     answers.append(0)
                    
#         return answers

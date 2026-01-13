class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
#         #1. Brute Force Approach
#         n = len(nums)
#         i = 0
#         while i < n:
#             if nums[i] == 0:
#                 nums.pop(i)
#                 nums.append(0)
#                 n -= 1
#             else:
#                 i += 1
# """
# Complexity:
# Time : O(n^2) - Pop shifts element
# Space: O(1)
# """
            # 2. Two pointer Approach
            n = len(nums)
            j = 0
            for i in range(n):
                if nums[i] != 0: # if 0 finds
                    nums[j], nums[i] = nums[i], nums[j] # swap
                    j += 1
                else:
                    pass

"""
Complexity:
Time : O(n) - Traversal
Space: O(1)
"""
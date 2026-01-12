class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left = 0

        for idx, val in enumerate(nums):
            if left == (tot - left - val):
                return idx
            left += val
        return -1
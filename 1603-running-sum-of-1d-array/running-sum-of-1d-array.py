class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # within the array
        n = len(nums)
        for i in range(1,n): # 1 -> n
            nums[i] += nums[i-1] #  cumulative = prev + curr
        return nums

"""
Complexity: 
Time : O(n)
Space: O(1)
"""
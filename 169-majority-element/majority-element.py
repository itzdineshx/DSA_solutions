class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = {}
        majority = n // 2 # threshold
        for i in nums:
            cnt[i] = cnt.get(i, 0) + 1
            if cnt[i] > majority:
                return i
"""
Complexity:
Time: O(n) - Traversal and Hash
Space: O(n) - Storing of element
"""
class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        diff = set()
        for term1, term2 in zip(nums, target):
            if term1 != term2:
                diff.add(term1)
                
        return len(diff)
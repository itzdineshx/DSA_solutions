class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            if nums[i]!=target[i]:
                l.append(nums[i])
        return len(set(l))
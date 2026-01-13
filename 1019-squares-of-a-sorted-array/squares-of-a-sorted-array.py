class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sort_arr = [num*num for num in nums]
        sort_arr.sort()
        return sort_arr
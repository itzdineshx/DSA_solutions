class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Approach 1: Brute Force(don't try)
        # nums[:] = (sorted(set(nums)))
        # return (len(nums))

        """
        Complexity:
        Time : O(n) - copy of array
        Space: O(1)
        """

        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return(j+1)

        """
        Complexity:
        Time : O(n) - Traversal
        Space: O(1)
        """
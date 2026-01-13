class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Appoach 1 - Brute force
        # return(s[::-1]) - returns err

        # Approach 3 - Two Pointer
        l ,r = 0 , len(s)-1
        while l < r: # Traverse
            s[l], s[r] = s[r], s[l] # swap
            l += 1 # increment left pointer
            r -= 1 # decrement right pointer
        return(s)

"""
Complexity:
Time: O(n) - Traversal through arr
Space: O(1) - Operations within arr
"""
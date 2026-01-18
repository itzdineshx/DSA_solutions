class Solution:
    def nextFreqGreater(self, arr):
        
        # optimal Solution - using stack
        from collections import Counter
        # Precompute the frequency
        freq = Counter(arr)
        
        n= len(arr)
        ans = [-1] * n
        stack = []
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Remove elements with frequency <= current
            while stack and freq[stack[-1]] <= freq[arr[i]]:
                stack.pop()
            # if no element to the right has a higher frequency
            if stack:
                ans[i] = stack[-1]
            # Push current element
            stack.append(arr[i])
        return ans
"""
Complexity:
Time: O(n) - Stack Operations
Space: O(n)
"""
        # Brute Force - T.L.E
        # from collections import Counter
        # # Precompute the frequency
        # frequency = Counter(arr)
        
        # n= len(arr)
        # ans = []
        # # checking freq with other elements
        # for i in range(n):
        #     found = False
        #     for j in range(i+1, n):
        #         if frequency[arr[j]] > frequency[arr[i]]:
        #             ans.append(arr[j]) # stores the greater element with higher freq
        #             found = True
        #             break
        #     # if no element to the right has a higher frequency
        #     if not found:
        #         ans.append(-1)
        # return ans
"""
Complexity:
Time: O(n^2) - Nested Loop
Space: O(n)
"""
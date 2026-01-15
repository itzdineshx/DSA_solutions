class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        """
        # Algorithm - Brute force`
        # 1. traverse throught the sub arr (i -> k)
        # 2. compute the average of given k size window
        # 3. return avg
        # """
        # n = len(nums)
        # max_avg = float('-inf')
        # for i in range(n - k+1):
        #     avg_sum = sum(nums[i:k+i]) / k
        #     max_avg = max(max_avg,avg_sum)
            
        # print(max_avg)

        """
        Complexity:
        Time: O(nk)
        Space: O(1)
        """

        # Maximum Average Subarray I
        """
        Algorithm – Sliding Window
        1. Compute the sum of the first k elements.
        2. Set this as the current maximum average.
        3. Slide the window from index k to n-1:
        - Add the current element to the sum.
        - Remove the element that moves out of the window.
        - Update the maximum average.
        4. Return the maximum average.
        """
        n = len(nums)
        cur_sum = 0
        for i in range(k): 
            cur_sum += nums[i] 
        max_avg = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            
            avg = cur_sum /k
            max_avg = max(max_avg,avg)
        return(max_avg)
"""
Complexity:
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        Algorithm:
        1. Start from the last point in the list(x1, y1).
        2. Repeatedly move to the next point(x2, y2).
        3. For each move from (x1, y1) to (x2, y2):
           - The minimum time required is: max(|x2 - x1|, |y2 - y1|)
        4. Accumulate and Return the total time.
        """
        # Appraoch 1: modifying points
        # min_time = 0
        # x1, y1 = points.pop()
        # while points:
        #     x2, y2 = points.pop()
        #     min_time += max(abs(x2-x1),abs(y2-y1))
        #     x1, y1 = x2, y2
        # return min_time

        # Appraoch 2: without modifying points
        min_time = 0
        n = len(points)
        for i in range(1,n):
            x1, y1 = points[i-1]
            x2, y2 = points[i]
            min_time += max(abs(x2-x1),abs(y2-y1))
        return min_time

"""
Complexity:
Time : O(n) - Traversal through points
Space : O(1) - Constant
"""
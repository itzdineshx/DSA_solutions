class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        """
        Algorithm:
        ----------
        1. Compute the total area of all squares.
        2. Set low to the as lower bound of y and high as the upper bound of y.
        3. While high - low is greater than precised val(10^-5):
            - Take mid = (low + high) / 2 and calc areas
            - If area below ≥ total area -> high = mid
            - Else move low = mid
        4. Return low.
        """
        total_area = sum(l * l for _, _, l in squares) # Total area of all squares

        # Binary search bounds
        low = min(y for _, y, _ in squares) # lower bound
        high = max(y + l for _, y, l in squares) # upper bound

        def area_below(H):
            area = 0.0
            for _, y, l in squares:
                if H <= y:
                    continue
                elif H >= y + l:
                    area += l * l
                else:
                    area += l * (H - y)
            return area

        # Balance point
        eps = 1e-6 # avoid overflow
        while high - low > eps:
            mid = (low + high) / 2
            if area_below(mid) >= total_area / 2:
                high = mid
            else:
                low = mid
        return low

"""
Complexity:
Time: O(n log r) - no of squares x area
space: O(1) - Constant
"""
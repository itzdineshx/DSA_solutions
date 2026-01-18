class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # matrix

        # prefix sums of matrix(rows, columns, diagonals)
        row = [[0]*(n+1) for _ in range(m)]
        col = [[0]*n for _ in range(m+1)]
        diag1 = [[0]*(n+1) for _ in range(m+1)]
        diag2 = [[0]*(n+2) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i+1][j] = col[i][j] + grid[i][j]
                diag1[i+1][j+1] = diag1[i][j] + grid[i][j]
                diag2[i+1][j] = diag2[i][j+1] + grid[i][j]

        def is_magic_sq(r, c, d):
            target = row[r][c+k] - row[r][c]

            # rows
            for i in range(r, r+k):
                if row[i][c+k] - row[i][c] != target:
                    return False
            # columns
            for j in range(c, c+k):
                if col[r+k][j] - col[r][j] != target:
                    return False
            # diagonals
            if diag1[r+k][c+k] - diag1[r][c] != target:
                return False
            if diag2[r+k][c] - diag2[r][c+k] != target:
                return False

            return True

        max_d = min(m, n)
        for k in range(max_d, 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic_sq(i, j, k):
                        return k
        return 1

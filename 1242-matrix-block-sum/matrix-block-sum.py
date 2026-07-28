class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        n = len(mat)
        m = len(mat[0])

        ans = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                total = 0

                for r in range(max(0, i-k), min(n, i+k+1)):
                    for c in range(max(0, j-k), min(m, j+k+1)):
                        total += mat[r][c]

                ans[i][j] = total

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
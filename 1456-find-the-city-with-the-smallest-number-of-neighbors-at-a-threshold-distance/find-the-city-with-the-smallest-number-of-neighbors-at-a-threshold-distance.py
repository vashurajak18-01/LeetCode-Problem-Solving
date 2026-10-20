import sys

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        adj_mat = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        for u, v, w in edges:
            adj_mat[u][v] = w
            adj_mat[v][u] = w

        for i in range(n):
            adj_mat[i][i] = 0

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if adj_mat[i] [via] != sys.maxsize and adj_mat[via][j] != sys.maxsize:
                        adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][via] + adj_mat[via][j])

        min_neigh = n
        city = -1
        for i in range(n): # City
            count = 0
            for j in range(n):
                if adj_mat[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_neigh:
                min_neigh = count
                city = i
                
        return city

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
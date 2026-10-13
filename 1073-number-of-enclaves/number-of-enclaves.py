from collections import deque

class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(row)]
        queue = deque()

        for r in range(row):
            for c in range(cols):
                if r == 0 or c == 0 or r == row - 1 or c == cols - 1:
                    if grid[r][c] == 1:
                        queue.append((r, c))
                        visited[r][c] = 1
        while  len(queue) != 0:
            i, j = queue.popleft()
            for x , y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_i , new_j = i+x, j+y
                if new_i < 0 or new_i >= row or new_j < 0 or new_j >= cols:
                    continue
                if grid[new_i][new_j] == 0:
                    continue
                if grid[new_i][new_j] == 1 and visited[new_i][new_j] == 1:
                    continue
                queue.append((new_i, new_j))
                visited[new_i][new_j] = 1

        count = 0
        for r in range(row):    
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count += 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
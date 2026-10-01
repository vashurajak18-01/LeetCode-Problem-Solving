class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
         
        if image[sr][sc] == color:
            return image

        rows = len(image)
        cols = len(image[0])
        initial_color = image[sr][sc]

        queue = deque()
        queue.append((sr, sc))

        # Mark as visited immediately
        image[sr][sc] = color

        while queue:
            i, j = queue.popleft()

            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i = i + x
                new_j = j + y

                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                if image[new_i][new_j] != initial_color:
                    continue

                # Mark visited when adding to queue
                image[new_i][new_j] = color
                queue.append((new_i, new_j))

        return image


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
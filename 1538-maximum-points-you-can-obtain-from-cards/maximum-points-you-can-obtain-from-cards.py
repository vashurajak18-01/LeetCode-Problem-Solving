class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        left_sum = 0
        right_sum =0

        for i in range(0, k):
            left_sum += cardPoints[i]

        max_sum = left_sum
        right_idx = n - 1
        for i in range(k-1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_idx]
            max_sum = max(max_sum, left_sum+right_sum)
            right_idx -= 1
        return max_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float('inf')
        for i in range(0, n):
            mini = min(mini, nums[i])
        return mini

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
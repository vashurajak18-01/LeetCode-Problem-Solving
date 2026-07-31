class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        n = len(nums)
        answer = float('-inf')

        for i in range(n):

            prefix = 1 if prefix == 0 else prefix
            suffix = 1 if suffix == 0 else suffix

            prefix *= nums[i]
            suffix *= nums[n - 1 - i]

            answer = max(answer, prefix, suffix)
        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
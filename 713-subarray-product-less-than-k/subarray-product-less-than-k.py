class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0

        count = 0
        left = 0
        prod = 1
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left + 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
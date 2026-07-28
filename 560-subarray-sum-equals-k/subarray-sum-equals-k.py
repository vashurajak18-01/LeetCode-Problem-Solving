class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = {0 : 1}
        
        for num in nums:
            prefix_sum += num

            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]

            freq[prefix_sum] = freq.get(prefix_sum, 0)+ 1

        return count

# ========================================================================
    # Brute Force Approch
        # count = 0

        # for left in range(len(nums)):
        #     sum = 0
        #     for right in range(left, len(nums)):
        #         sum += nums[right]
        #         if sum == k:
        #             count += 1

        # return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
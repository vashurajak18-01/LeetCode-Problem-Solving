class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = 0
        max_ans = 0
        j = 0
        while j < len(nums):
            if nums[j] == 1:
                curr_count += 1
            else:
                max_ans = max(max_ans, curr_count)
                curr_count = 0
            j += 1
        return max(max_ans, curr_count)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
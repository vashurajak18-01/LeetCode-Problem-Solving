class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [0]*n
        pos_idx, neg_idx = 0, 1

        for i in range(0, n):

            if nums[i] >= 0:
                result[pos_idx] = nums[i]
                pos_idx += 2
                
            else: 
                result[neg_idx] = nums[i]
                neg_idx += 2

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
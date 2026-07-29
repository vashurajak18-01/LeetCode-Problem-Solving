class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map = {0:-1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            rem = prefix_sum % k

            if rem in rem_map:
                if i - rem_map[rem] >=2:
                    return True
            else:
                rem_map[rem] = i
        
        return False

        
        # ------------------------------------------------------------------------
        # Brute Force Approch
        # n = len(nums)

        # for i in range(n-1):
        #     sum = nums[i]
        #     for j in range(i+1, n):
        #         sum += nums[j]

        #         if sum % k == 0:
        #             return True 
        # return False





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
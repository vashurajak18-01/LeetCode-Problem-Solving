class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       
        # left = 0
        # zero_count = 0
        # max_length = 0

        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         zero_count += 1
            
        #     while zero_count > k:
        #         if nums[left] == 0:
        #             zero_count -= 1 
        #         left += 1 
            
        #     max_length = max(max_length, right - left + 1)
        
        # return max_length
# ===============================================================================
        # maxi = 0
        # left = right = 0
        # zeroes = 0

        # while right < len(nums):
        #     if nums[right] == 0:
        #         zeroes += 1
        #     while zeroes > k:
        #         if nums[left] == 0:
        #             zeroes -= 1
        #         left += 1
        #     if zeroes <= k:
        #         maxi = max(maxi, right - left + 1)
        #     right += 1
            
        # return maxi


# ================================================================================
        maxi = 0
        left = right = 0
        zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            if zeroes <= k:
                maxi = max(maxi, right - left + 1)
            right += 1
            
        return maxi


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
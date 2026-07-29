class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        for i in range(1,len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right_prod
            right_prod *= nums[i]

        return ans

    # --------------------------------------------------------------------------------------------------    
    # Brute Force Approach    
        # res= []
        # for i in  range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
                
        #         product *= nums[j] 
        #     res.append(product)
        # return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
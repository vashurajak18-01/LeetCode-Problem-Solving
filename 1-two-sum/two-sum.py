class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}  
        for i in range(len(nums)):
            
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]

            dict[nums[i]] = i
            
        return [] 

       


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
    
        if  n == 1: 
            return 1
    
        i = 0
        j = i+1 
        while j < n:
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[j]
    
            j += 1
        return i + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
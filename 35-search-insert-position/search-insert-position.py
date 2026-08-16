class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        insert_pos = n
        low = 0
        high = n - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                insert_pos = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return insert_pos

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
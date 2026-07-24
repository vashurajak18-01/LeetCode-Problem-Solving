class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        sum = 0
        left =  0

        for right in range(0,len(nums)):
            sum += nums[right]

            while sum >= target:
                minLength = min(minLength, right - left + 1)
                sum -= nums[left]
                left += 1
            
        return 0 if minLength == float('inf') else minLength
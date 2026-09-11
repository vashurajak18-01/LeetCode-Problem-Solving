# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         last_index = len(nums) -1

#         def func(index, jump):
#             if index >= last_index:
#                 return jump
            
#             min_jump = float('inf')

#             for i in range(1, nums[index]+1):
#                 min_jump = min(min_jump, func(index+i, jump+1))

#             return min_jump
        
#         return func (0,0)

#  ===================================================================================


class Solution:
    def jump(self, nums: List[int]) -> bool:
        last_index = len(nums) -1
        dp = [-1]*len(nums)

        def func(index ):
            
            if index >= last_index:
                return 0
            
            if dp[index] != -1:
                return dp[index]
            
            min_jump = float('inf')

            for i in range(1, nums[index]+1):
                min_jump = min(min_jump, 1 + func(index + i))

            dp [index] = min_jump

            return dp [index]
        
        return func (0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
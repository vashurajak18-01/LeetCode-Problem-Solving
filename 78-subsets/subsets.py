class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        to_subsets = 1 << n
        answer = []

        for num in range(to_subsets):
            lst = []
            for i in range(n):
                if num & (1 << i) != 0:
                    lst.append(nums[i])
            
            answer.append(lst)
        return answer

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
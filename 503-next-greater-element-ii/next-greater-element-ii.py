class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]* n
        stack = []

        for i in range((2 * n) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums[i % n]:
                stack.pop()
            if i < n:
                if len(stack) != 0:
                    ans[i] = stack[-1]

            stack.append(nums[i % n])

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num:
            num = num // 2 if num % 2 == 0 else num -1
            step += 1
        
        return step

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
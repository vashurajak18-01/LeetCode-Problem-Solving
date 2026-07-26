class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            max_len = max(max_len, right-left+1)
        
        return max_len

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
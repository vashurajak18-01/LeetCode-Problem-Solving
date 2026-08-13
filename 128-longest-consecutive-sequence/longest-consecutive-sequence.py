class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()

        for num in nums:
            my_set.add(num)

        longest = 0
        count = 0

        for num in my_set:
            
            if num-1 not in my_set:
                x = num
                count = 1

                while x+1 in my_set:
                    count += 1
                    x += 1
                    
                longest = max(longest, count)

        return longest

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen = set()
        # left = 0
        # max_len = 0

        # for right in range(len(s)):
        #     while s[right] in seen:
        #         seen.remove(s[left])
        #         left += 1

        #     seen.add(s[right])
        #     max_len = max(max_len, right - left + 1)

        # return max_len

# ==============================================================================

        maxi = 0
        my_dict = dict()
        left = right = 0

        while right < len(s):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]]+1)

            maxi = max(maxi, right - left + 1)
            my_dict[s[right]] = right
            right += 1

        return maxi

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
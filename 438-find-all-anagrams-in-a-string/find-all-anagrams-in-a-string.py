class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p):
            return res

        pMap = {}
        sMap = {}

        # Build frequency map for string p
        for c in p:
            pMap[c] = pMap.get(c, 0) + 1

        left = 0
        count = len(p)

        # Sliding window over string s
        for right in range(len(s)):
            ch = s[right]

            # Add current character to sMap
            sMap[ch] = sMap.get(ch, 0) + 1

            # If the character matches the required count in pMap, decrement count
            if ch in pMap and sMap[ch] <= pMap[ch]:
                count -= 1

            # Shrink the window from the left if it exceeds length of p
            if right - left + 1 > len(p):
                leftChar = s[left]
                if leftChar in pMap and sMap[leftChar] <= pMap[leftChar]:
                    count += 1
                sMap[leftChar] -= 1
                left += 1

            # If count reaches 0, an anagram is found
            if count == 0:
                res.append(left)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
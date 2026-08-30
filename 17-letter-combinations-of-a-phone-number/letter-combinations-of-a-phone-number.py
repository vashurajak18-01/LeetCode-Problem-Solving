class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        result = []

        def backtrack(index, subset):
            if index >= len(digits):
                result.append("".join(subset))
                return

            for ch in phone[digits[index]]:

                subset.append(ch)
                backtrack(index+1, subset)

                subset.pop()           
            
        backtrack(0,[])
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
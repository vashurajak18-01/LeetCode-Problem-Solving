class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        brackets = [""]*(n*2)

        def solve(idx, total):

            if idx >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return
        
            if total > len(brackets)//2:
                return
            elif total == -1:
                return
            brackets[idx] = "("
            solve(idx+1, total + 1)

            brackets[idx] = ")"
            solve(idx+1, total-1)

        solve(0, 0)

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
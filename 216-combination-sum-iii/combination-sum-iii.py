class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def solve(last, total, subset):
            if total == n and len(subset) == k:
                result.append(subset.copy())
                return
            if total > n or len(subset) > k:
                return
                

            for i in range(last, 10):
                sum = total+i
                subset.append(i)

                solve(i+1, sum, subset)
                subset.pop()

        solve(1, 0, [])
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
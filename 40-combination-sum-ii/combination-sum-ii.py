class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def solve(index, total, subset):

            if total == 0:
                result.append(subset.copy())
                return
            if total < 0:
                return

            if index >= len(candidates):
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                subset.append(candidates[i])
                sum = total - candidates[i]
                solve(i+1, sum, subset)
                subset.pop()

        solve(0,target,[])
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
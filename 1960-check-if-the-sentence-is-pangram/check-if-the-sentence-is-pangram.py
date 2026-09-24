class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)
        return len(seen) == 26
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
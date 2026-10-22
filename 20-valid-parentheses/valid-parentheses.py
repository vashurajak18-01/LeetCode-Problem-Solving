class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if not stack:
                    return False

                if i == ")" and stack.pop() != "(":
                    return False
                if i == "]" and stack.pop() != "[":
                    return False
                if i == "}" and stack.pop() != "{":
                    return False

        return len(stack) == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
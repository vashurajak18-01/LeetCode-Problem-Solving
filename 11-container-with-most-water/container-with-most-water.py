class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        left = 0
        right = n - 1

        while(left < right):
            length = min(height[left], height[right])
            width = right-left
            area = length * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
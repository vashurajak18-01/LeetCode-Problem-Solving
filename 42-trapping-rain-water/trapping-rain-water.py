class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        totalWater = 0

        while(left < right):
            if leftMax < rightMax:
                left+=1
                leftMax = max(leftMax, height[left])
                totalWater += leftMax - height[left]
                
            else:
                right-=1
                rightMax = max(rightMax, height[right])
                totalWater += rightMax - height[right]
        
        return totalWater

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
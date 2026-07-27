
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        queue = deque()
        for i in range(len(nums)):
            while (
                queue and nums[queue[-1]] <= nums[i]
            ):
                queue.pop()

            while (
                queue and i - queue[0] >= k
            ):
                queue.popleft()
            
            queue.append(i)
            if i+1 >= k:
                answer.append(nums[queue[0]])

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
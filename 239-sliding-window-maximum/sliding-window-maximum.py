from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n =len(nums)

        result = [0] * (n-k+1)
        _deque_ = deque()

        for right in range(n):

            while _deque_ and _deque_[0] <= right - k:
                _deque_.popleft()
            while _deque_ and nums[_deque_[-1]] < nums[right]:
                _deque_.pop()
            _deque_.append(right)

            if right >= k-1:
                result[right-k+1] = nums[_deque_[0]]

        return result 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi = float('-inf')
        def solve(node):
            nonlocal maxi
            if node is None:
                return 0
            left_sum = solve(node.left)
            if left_sum < 0:
                left_sum = 0

            right_sum = solve(node.right)
            if right_sum < 0:
                right_sum = 0
            maxi = max(maxi, left_sum + node.val + right_sum)

            return node.val + max(left_sum, right_sum)

        solve(root)
        return maxi

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
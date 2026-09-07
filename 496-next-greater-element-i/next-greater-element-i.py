class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        dictionary = {}

        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            
            if stack:
                dictionary[nums2[i]] = stack[-1]
            else:
                dictionary [nums2[i]] = -1
            stack.append(nums2[i])
        for y in nums1:
            if y in dictionary:
                ans.append(dictionary[y])
        return ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
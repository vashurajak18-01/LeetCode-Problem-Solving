class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mini = float('inf')
        sumi = 0

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return sum
                elif sum < target:
                    l += 1
                else :
                    r -= 1

                diff = abs(sum - target)  
                if diff < mini:
                    mini = diff
                    sumi = sum
        return sumi
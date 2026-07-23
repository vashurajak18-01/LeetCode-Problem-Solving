class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ===================================================================================
        
        # nums.sort()

        #====================================================================================
        
        # count0 = 0
        # count1 = 0
        # count2 = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count0 += 1
        #     elif nums[i] == 1:
        #         count1 += 1
        #     else:
        #         count2 += 1
        # idx = 0
        # for i in range(count0):
        #     nums[idx] = 0
        #     idx += 1
        # for i in range(count1):
        #     nums[idx] = 1
        #     idx += 1
        # for i in range(count2):
        #     nums[idx] = 2
        #     idx += 1

        # ====================================================================================

        # Using Dutch National Flag Algorithm
        low = mid = 0
        high = len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid] = nums[mid], nums[low]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid += 1
            elif nums[mid]==2:
                nums[mid], nums[high]=nums[high], nums[mid]
                high-=1


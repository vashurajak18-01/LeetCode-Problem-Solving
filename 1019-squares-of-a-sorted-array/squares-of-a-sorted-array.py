class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # sorter way to solve 
        nums = list(map(lambda x:x*x,nums))
        return sorted(nums)

        # Simple and easy approach
        # result = []
        # for num in nums:
        #     result.append(num*num)
        # result.sort()
        # return result

        # Long Method
        # nums.sort()
        # neg = []
        # pos = []
        # n = len(nums)

        # for num in nums:
        #     if num < 0:
        #         neg.append(num)
        #     else:
        #         pos.append(num)
        # if len(neg) == 0:
        #     return [x*x for x in pos]
        # if len(pos) == 0:
        #     return [x*x for x in neg] [::-1]

        # neg = [x*x for x in neg][::-1]
        # pos = [x*x for x in pos]
        # i=j=0
        # result = []
        # while i < len(neg) and j< len(pos):
        #     if neg[i] < pos[j]:
        #         result.append(neg[i])
        #         i += 1
        #     else:
        #         result.append(pos[j])
        #         j += 1
        # while i < len(neg):
        #     result.append(neg[i])
        #     i+=1
        # while j < len(pos):
        #     result.append(pos[j])
        #     j+=1
        # return result
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
        
        # carry = 0
        # result = ""
        # a, b = list(a), list(b)
        # while a or b or carry == 1:
        #     if a:
        #         carry += int(a.pop())
        #     if b:
        #         carry += int(b.pop())
        #     result += str(carry % 2)
        #     carry = carry // 2
        
        # return result[: :-1]
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x   # Copy 
        sum = 0
        while x > 0:
            digit = x % 10

            # Constraints Given
            if sum > (2**31 -1 -digit) //10:
                return False

            sum = sum * 10 + digit
            x = x // 10
        
        return original == sum
        
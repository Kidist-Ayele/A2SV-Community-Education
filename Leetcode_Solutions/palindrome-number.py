class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        y = 0
        while num:
            modulo = num % 10
            y *= 10
            y += modulo
            num //= 10
        return x == y
# Link: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31+1 or x <= -2**31:
            return 0
        else:
            rev = 0
            if x > 0:
                while x != 0:
                    digit =x%10
                    rev = rev*10 + digit
                    x = x//10
                if rev >= 2**31-1 or rev <= -2**31:
                    return 0
                else:
                    return rev
            else:
                x = -x
                while x != 0:
                    digit = x %10
                    rev = rev*10 + digit
                    x = x//10
                if rev >= 2**31-1 or rev <= -2**31:
                    return 0
                else:
                    return -(rev)
     
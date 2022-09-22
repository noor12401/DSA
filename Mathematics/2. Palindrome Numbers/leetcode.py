# Link: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp_x = x
        while (temp_x>0):
            rev = rev*10 + temp_x%10
            temp_x = int(temp_x/10)
        return (x == rev)
        
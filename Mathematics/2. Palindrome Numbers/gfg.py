#Link: https://practice.geeksforgeeks.org/problems/palindrome0746/1

class Solution:
    def is_palindrome(self, n):
        rev = 0
        temp_n = n
        while (temp_n>0):
            rev = rev*10 + temp_n%10
            temp_n = int(temp_n/10)
        if (rev == n):
            return "Yes"
        else:
            return "No"

# Link: https://practice.geeksforgeeks.org/problems/reverse-bits3556/1

class Solution:
    def reversedBits(self, X):
        x = '{:032b}'.format(X)
        rev = ""
        for i in range(1, len(x)+1):
            rev += x[-i]
        return int(rev, 2)
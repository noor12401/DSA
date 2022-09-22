# Link: https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1

class Solution:
    def lcmAndGcd(self, A , B):
        n1 = max(A, B)
        n2 = min(A, B)
        def gcd(n1, n2):
            if n2 == 0:
                return n1
            else:
                return gcd(n2, n1%n2)
        GCD = gcd(n1, n2)
        LCM = (A*B)//GCD
        return LCM, GCD
## Find the GCD of two numbers

# Input: 4, 8
# Output: 4
# Explanation: 4 is the highest number that can divide both 4 and 8.

num1 = 30
num2 = 40

# Approach 1: Bruteforce
result = 0
for i in range(max(num1, num2), 0, -1):
    if num1%i == 0 and num2%i == 0:
        result = i
        break
    else:
        continue
print(result)
# Complexity: Time - O(N), Space - O(1)


# Approach 2: Using Euclidean Algorithm
# Check this article to understand: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
# Note: Make sure n1 > n2
def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1%n2)
print(gcd(270, 192))
print(gcd(40, 30))
# Complexity: Time - O(log2(n)) where n = max(num1, num2), Space - O(1)

## LCM
'''
To calculate LCm, you can either use formula or you can use the GCD to calculate LCM
LCM = (Num1 * Num2) / GCD(Num1, Num2)
'''



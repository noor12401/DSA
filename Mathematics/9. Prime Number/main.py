import math
## Check for a Prime number

# Input: 13
# Output: True
# Input: 56
# Output: False

n1 = 56
n2 = 123

n = n2

# Approach 1: Bruteforce
def check_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
print(check_prime(n))
# Complexity - Time: O(n)

# Approach 2: Pairing

def check_prime2(n):
    for i in range(2, math.floor(math.sqrt(n))):
        if n%i == 0:
            return False
    return True
print(check_prime2(n))
'''
Explanation: We know if a number is divisble then it will have pairs. For example:
Number = 30 = (1, 30) (2, 15) (3, 10) (5, 6) <> (6, 5) (10, 3) (15, 2) (30, 1)
Thus instead of going to every range, we can search for sqrt(30) which is approax 5, so we can check dividing 30 from 1 to 5.
'''
# Complexity: Time - O(sqrt(n))


## Aproach 3: mMore Efficient Way!
'''
Let's take a number 1020, So numbers that can divide 1020 are:
1, 2, 3, 4, 5, 6, 10, 12, 15, 17, 20, 30, 34, 51, 60, 68, 85, 102, 170, 204, 255, 340, 510, 1020
Now sqrt(1020) is 32. So if we use previous method, we can check for these numbers only.
1, 2, 3, 4, 5, 6, 10, 12, 15, 17, 20, 30 Now we reduce multiple of 2 and 3 then we are left with:
5 and 17. here we are eliminating multiples of 2 and 3 meaning if we see a number is divisible by 2 then we will not check for 4,6,8 and so on..
And if the number is divisible by 3 then we will not check for 6, 9, 12, and so on..
Also we will start with 5 and will increament by 6 so here we are jumping and reducing iterations.

'''
def check_prime3(n):
    if (n%2 == 0 or n%3 == 0):
        return False
    for i in range(5, math.floor(math.sqrt(n))+1, 6):
        if (n%i == 0 or n%(i+2)):
            return False
    return True
print(check_prime3(n))
# Complexity: Time - Approx 3 times faster than O(sqrt(n))



import math
## Count the number of digits in factorial
# Input: 8
# Output: 5
# Explanation: Factorial of 6 is 40320. And the lenght of 40320 is 5.

## Approach 1: Bruteforce and using len()
def fact1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return len(str(result))
print(fact1(8))
# Complexity: Time - O(n+m) where n is for loop and m is len(), Space - O(1)

## Approach 2: Bruteforce and using log10
def fact2(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return math.floor(math.log10(result)+1)
print(fact2(8))
# Complexity: Time - O(n), Space- O(1)

'''
Theoretically Approach 1 and Approach 2 has same time complexity but practically Approach 2 ie better
'''

## Approach 3: Calculate length without calcuating Factorial
'''
We know factorial of n is n!.
So if n is 5 then we have 5*4*3*2*1 = 120 (Length is 3)
To calculate length we use log10. So we can say length of n! = log10(n!)+1
So log10(5!)+1 = log10(5*4*3*2*1)+1 = 3
We know log10(a*b) = log10(a) + log10(b)
So, our formula becomes: For finding length of digits of a factorial of n will be
length(n!) = log10(1)+log10(2)+log10(3)+....+log10(n)+1
'''
def fact3(n):
    result = 0
    for i in range(1, n+1):
        result += math.log10(i)
    return math.floor(result)+1
print(fact3(8))
# Complexity: Time - O(n), Space - O(1)





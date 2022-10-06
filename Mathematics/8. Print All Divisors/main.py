import math
## Print All Divisors
# Input: 36
# Output: 1 2 3 4 6 9 12 18 36

## Approach 1: Bruteforce
num = 36
for i in range(1, num+1):
    if num%i == 0:
        print(i, end =" ")
print("\n")
# Complexity: Time - O(n), Space - O(1)

## Approach 2
'''
For 36 we have [1, 2, 3, 4, 6, 9, 12, 18, 36]
If we observe we see 36/2 = 18, therefore both 2 and 18 are Divisors
36/3 = 12, so both 3 and 12 are Divisors
36/4 = 9 so both 4 and 9 are Divisors
36/5 does not give remainder as zero so we take 36/6
36/6 = 6 now here remainder and quotient both are 6 so we will stop here.
If you see we have got all the divisros. In this approach we only need to iterate sqrt(n) times.
sqrt(36) is 6 so we iterate from 1 to 6 and print both the remainder and quotient
'''
n = 42
for i in range(1, math.floor(math.sqrt(n))+1):
    if n%i == 0:
        print(i, end=" ")
        if n//i != i: ## This check is required so that we don't print the last number twice.
            print(n//i, end = " ")
# Complexity: Time - O(sqrt(n)), Space - O(1)
            
            
            
        
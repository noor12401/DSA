### Factorial of a number
# Input: 5
# Output: 5*4*3*2*1 = 120

n = 6

# Approach 1:
result = 1
for i in range(1, n+1):
    result *= i
    i+= 1
print(result)
# Complexity: Time - O(n), Space - O(1) 

## Aproach 2:
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(n))
# Complexity: Time - O(n), Space - O(n)
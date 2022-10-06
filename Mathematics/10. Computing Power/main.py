import math
## Computing Power
# Input: (2, 3)
# Output: 8
# Explantion: 3 times 2 is 8. 2*2*2 = 8

# Input: (3, 6)
# Output: 729
# Explantion: 6 times 3 is 729. 3*3*3*3*3*3 = 729

## Approach 1: Bruteforce
def compute_power1(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result
print(compute_power1(3, 6))
# Complexity: Time - O(n), Space - O(1)

## Approach 2: Using square functions
def compute_power2(a, b):
    return a**b
print(compute_power2(3, 6))
# Complexity: Time - O(log(b)), Space - O(1)

## Approach 3: Using inbuilt math.pow function
def compute_power3(a, b):
    return int(math.pow(a, b))
print(compute_power3(3, 6))
# Complexity: Time - O(1), Space - O(1)
'''
We see Approach 3 > Approach 2. To know why math.pow(a, b) is better than a**b. Read this article
https://stackoverflow.com/questions/48839772/why-is-time-complexity-o1-for-powx-y-while-it-is-on-for-xy
'''






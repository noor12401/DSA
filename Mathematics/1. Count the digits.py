## Count the digits

# Input: 2352
# output: 4
# Explanation: There are 4 digits so output is 4

n = 2352

## Approach 1
print("By Approach 1: ", len(str(n)))
# Time Complexity: len() has o(1) whereas str() takes O(n) as per Python docs. So overall is O(n)

## Aproach 2
count = 0
for i in str(n):
    count+= 1
print("By Approach 2: ", count)
# Time Complexity: O(n)

## Aproach 3
res = 0
while n>0:
    n = int(n/10)
    res += 1
print("By Approach 3: ", res)
# Time Complexity: O(n)
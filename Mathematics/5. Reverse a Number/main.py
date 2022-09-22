## Reverse a number
# Input: 123
# Output: 321

n = 786

## Approach 1:
res = ""
for i in range(0, len(str(n))):
    res += str(n%10)
    n = n//10
print(res)
# Complexity: Time - O(n), Space - O(1)

m = 123
## Aproach 2:
for i in range(1, len(str(m))+1):
    print(str(m)[-i], end="")
# Basically we are printing -1, -2 and -3 element of n. In python n[-1] is 6, n[-2] is 8 and n[-3] is 7. This is reverse indexing.
# Complexity: Time - O(n), Space - O(1)

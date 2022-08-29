### Palindrome Number
# Input: 78687
# Ouput: True
# Explanation: The number remains the same when its digits are reversed.

n = 78687

## Approach 1
pointer = len(str(n))
reversed_n = ""
while (pointer>0):
    reversed_n += str(n)[pointer-1]
    pointer -= 1
print(str(n) == reversed_n)
# Time Complexity: O(n)
    
## Approach 2
rev = 0
temp_n = n
while (temp_n>0):
    rev = rev*10 + temp_n%10
    temp_n = int(temp_n/10)
print(rev == n)
# Time Complexity: O(n)
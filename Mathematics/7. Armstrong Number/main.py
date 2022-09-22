## Armstrong Number

# Input: 1634
# Output: True

num = 1407

# Approch 1: Bruteforce
l = len(str(num))
result = 0
for i in str(num):
    result += int(i)**l
print(result == num)
# Complexity: Time - O(N), Space - O(1)

'''
Approach 2 - You can use log10(number)+1 instead of len() to count digits
Approach 3 - Instead of using inbuilt function like log10 or len(). you can divide number by 10 and count the numbers.
'''
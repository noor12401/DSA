## Count trailing zeros of factorial
# Input: 10
# Output: 2
# Explanation: Since factorial of 10 is 3628800 and it has two zeros at the end of the number. So output is 2

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        i+= 1
    return result

n = 251
fact = factorial(n)

## Aproach 1:
count = 0
while True:
    for i in range(len(str(fact))-1, -1, -1): # This means for (i=6, i>-1, i--). Reversing a string
        # We will compare last number. If it is zero, increase count and if not then stop the for loop and break the while. This way we will not compare all the zeros but only last zeros.
        if(str(fact))[i] == "0":
            count += 1
        else:
            break
    break
print(count)
# Time Complexity: O(n)

## Aproach 2:
result = 0
while fact%10 == 0:
    result += 1
    fact = fact//10
print(result)
# Time Complexity: It's clearly much less than O(n) but it will create overflow in memory if we compute factorial for large numbers.

## Aproach 3:
# Explanation: https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
res = 0
while n>=5:
    n = n//5
    res += n
print(res)



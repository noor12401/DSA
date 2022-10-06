# Problem Link: https://www.codechef.com/problems/FCTDIG

# cook your code here
import math
def fact(n):
    result = 0
    for i in range(1, n+1):
        result += math.log10(i)
    return math.floor(result)+1
t = int(input())

while t:
    g = int(input())
    n = list(map(int, input().split(" ")))
    for j in n:
        print(fact(n), end=" ")
    print()
    t -= 1
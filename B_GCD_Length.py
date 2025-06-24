from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    a,b,c= map(int, input().split())
    num1 = a - (c-1)
    num2 = b - (c-1)
    if a < b:
        print(10 ** (c-1) * (10 ** (min(num1 , num2)) - 1) , 10 **(c-1) * (10 ** (max(num1 , num2)-1)))
    elif a >b:
        print(10 ** (c-1) * (10 ** (max(num1 , num2)) - 1) , 10 **(c-1) * (10 ** (min(num1 , num2)-1)))
    else:
        print(10 ** (c-1) * (10 ** (num1 - 1)) , 10 **(c-1) * (10 ** (num1 - 1) + 1))
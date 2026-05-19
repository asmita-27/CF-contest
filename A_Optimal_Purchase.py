from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,a,b = map(int, input().split())
    res = 0
    if a*n<b:
        res = a*n
    # elif a*n==b:
    #     res = a*n
    elif a*n>b:
        if n>=3:
            res = b*(n//3)+a*(n%3)
        else:
            res = b
            
    print(res)
    
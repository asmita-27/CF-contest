from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if all(x == a[0] for x in a):
        print(0)
        continue

    a  = a + a 
    curr = 1
    mxLen = 0
    
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            curr +=1
        else:
            mxLen = max(mxLen, curr)
            curr = 1
    mxLen = max(mxLen, curr)
    mxLen = min(mxLen, n)
    print((mxLen+1)//2)

    
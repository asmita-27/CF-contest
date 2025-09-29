from collections import defaultdict, Counter, deque
import os
import math
import sys  


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
     
    uniQ = []
    for x in a:
        if not uniQ or uniQ[-1] != x:
            uniQ.append(x)
    n = len(uniQ)
    
    ans = n
    for i in range(n - 2):
        if uniQ[i] < uniQ[i+1] < uniQ[i+2]:
            ans -= 1
        elif uniQ[i] > uniQ[i+1] > uniQ[i+2]:
            ans -= 1
    print(ans)
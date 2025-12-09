from collections import defaultdict, Counter, deque
import os
import math
import sys

def getR(a):
    while a % 2 == 0:
        a //= 2
    return a
    
for _ in range(int(input())):
    a,b = map(int, input().split())
    if a>b:
        a,b = b,a
    ra = getR(a)
    rb = getR(b)
    if rb!=ra:
        print(-1)
        continue
    ans = 0
    b//=a
    
    while b>=8:
        b//=8
        ans+=1 
    if b>1:
        ans+=1
    print(ans)


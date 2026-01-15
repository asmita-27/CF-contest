from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    x = [0]*n
    for i in a:
        x[i-1] += 1
    x.sort()
    s = sum(x)
    ans= s
    for i in range(n):
        ans= min(ans, s-(n-i)*x[i])
    print(n-ans)    
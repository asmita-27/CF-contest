from collections import defaultdict, Counter, deque
import os
import math
import sys
from bisect import bisect_left 

def leng(arr):
    lis = []
    for x in arr:
        pos = bisect_left(lis, x)
        if pos == len(lis):
            lis.append(x)
        else:
            lis[pos] = x
    return len(lis)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a2 = a+a 
    ans = 1
    for s in range(n):
        arr = a2[s:s+n]
        ans = max(ans, len(set(arr)))
    print(ans)
    
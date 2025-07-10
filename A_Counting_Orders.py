from collections import defaultdict, Counter, deque
import os
import math
import sys
import bisect
MOD = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort(reverse=True)
    
    res = 1
    for i in range(n):
        x = len(a)-bisect.bisect_right(a, b[i])
        res = res * (max(x-i, 0))%MOD
    print(res)
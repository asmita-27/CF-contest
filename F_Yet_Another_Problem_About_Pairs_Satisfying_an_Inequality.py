from collections import defaultdict, Counter, deque
import os
import math
import sys
import bisect

MOD = 10**9 + 7
mx = 200007
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    v = []
    for i in range(n):
        if a[i]>= i+1:
            continue
        res += bisect.bisect_left(v, a[i])
        bisect.insort(v, i+1)
    print(res)
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    res = n
    i = 0
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        res = min(res, max(i, n - j))
        if j < n:
            res = min(res, max(j, n - j))
        i = j
    print(res)
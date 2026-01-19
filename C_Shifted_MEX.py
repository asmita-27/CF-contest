from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = -a[i]
        s = set()
        for j in range(n):
            s.add(a[j] + x)
        mexVal = 0
        while mexVal in s:
            mexVal += 1
        ans = max(ans, mexVal)
    print(ans)
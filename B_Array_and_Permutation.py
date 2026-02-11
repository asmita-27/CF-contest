from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    flg = True
    for i in range(n):
        if a[i] == p[i]:
            continue
        ok = False
        if i > 0 and p[i-1] == a[i]:
            ok = True
        if i < n-1 and p[i+1] == a[i]:
            ok = True
        if not ok:
            flg = False
            break
    print("YES" if flg else "NO")
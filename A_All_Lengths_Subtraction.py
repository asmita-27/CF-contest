from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l, r = 0, n - 1
    ok = True
    for i in range(1, n + 1):
        if l <= r and a[l] == i:
            l += 1
        elif l <= r and a[r] == i:
            r -= 1
        else:
            ok = False
            break
    print("YES" if ok else "NO")

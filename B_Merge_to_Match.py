from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    flg = True
    if n < 2 * m:
        flg = False
    else:
        for i in range(m):
            if not (a[i] < b[i] < a[n - m + i]):
                flg = False
                break
    print("YES" if flg else "NO")
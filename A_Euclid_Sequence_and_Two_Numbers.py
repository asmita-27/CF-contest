from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        a.sort(reverse=True)
        print(a[0], a[1])
        continue
    a.sort(reverse=True)
    flg = True
    for i in range(n - 2):
        if a[i] % a[i + 1] != a[i + 2]:
            flg = False
            break
    if flg:
        print(a[0], a[1])
    else:
        print(-1)
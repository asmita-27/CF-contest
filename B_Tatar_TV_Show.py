from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int, input().split())
    s = input()
    flg = True
    for r in range(k):
        cnt = 0
        for i in range(r, n, k):
            if s[i] == '1':
                cnt += 1
        if cnt % 2:
            flg = False
            break
    print("YES" if flg else "NO")
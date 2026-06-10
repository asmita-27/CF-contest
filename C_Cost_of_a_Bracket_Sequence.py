from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    stk = []
    pairs = []
    for i, ch in enumerate(s):
        if ch == '(':
            stk.append(i)
        elif stk:
            pairs.append((stk.pop(), i))
    d = min(k, len(pairs))
    ans = ['0'] * n
    for i in range(d):
        l, r = pairs[i]
        ans[l] = '1'     
    print(''.join(ans))
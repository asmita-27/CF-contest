from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, t, s = map(int, input().split())
    S = input().strip()
    l = 0
    r = 0
    ans = 0
    for c in S:
        if c == 'A':
            if t * s == ans:
                continue
            ans += 1
            if ans > l * s:
                l += 1
            r = min(t, r + 1)
        elif c == 'I':
            if l == t:
                continue
            ans += 1
            l += 1
            r = min(t, r + 1)
        elif c == 'E':
            if ans == r * s:
                continue
            ans += 1
            if ans > l * s:
                l += 1
    print(ans)
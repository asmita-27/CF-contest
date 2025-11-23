from collections import defaultdict, Counter, deque
import os
import math
import sys

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ok = True
    s = 0
    for x in a:
        s += x
        if s <= 0:
            ok = False
            break
    if ok:
        s = 0
        for x in reversed(a):
            s += x
            if s <= 0:
                ok = False
                break

    print("YES" if ok else "NO")

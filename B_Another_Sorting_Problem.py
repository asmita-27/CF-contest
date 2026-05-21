from collections import defaultdict, Counter, deque
import os
import math
import sys



for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = 1
    r0 ,r1 = float("inf"), float("inf")

    for x, y in zip(a, a[1:]):
        if x < y:
            r0 = max(r0, min(r1, y - x))
        elif x > y:
            l = max(l, x - y)
            r1 = r0
            r0 = l - 1
    print("YES" if r1 >= l else "NO")
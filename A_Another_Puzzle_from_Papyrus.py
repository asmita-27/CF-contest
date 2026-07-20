from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,c = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = float('inf')

    if all(x >= y for x, y in zip(a, b)):
        ans = sum(x - y for x, y in zip(a, b))

    sa = sorted(a)
    sb = sorted(b)
    if all(x >= y for x, y in zip(sa, sb)):
        ans = min(ans, c + sum(a) - sum(b))
    if ans != float('inf'):
        print(ans)
    else:
        print(-1)
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, s = map(int, input().split())
    ans = 0

    for _ in range(n):
        dx, dy, xi, yi = map(int, input().split())
        if dx == dy:
            ans += (xi == yi)
        else:
            ans += (xi + yi == s)

    print(ans)
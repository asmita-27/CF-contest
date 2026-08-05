from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a = list(map(int, input().split()))
    ans = 0
    while len(set(a)) == 3:
        mx = a.index(max(a))
        mn = a.index(min(a))
        a[mx] -= 1
        a[mn] += 1
        ans += 1
    print(ans)
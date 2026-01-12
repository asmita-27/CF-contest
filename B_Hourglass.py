from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s, k, m = map(int, input().split())
    idx = m // k
    L = idx * k
    d = m - L
    if s <= k:
        r_last = s
    else:
        r_last = s if (idx % 2 == 0) else k
    ans = max(0, r_last - d)
    print(ans)
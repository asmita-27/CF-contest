from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = sorted(a)
    u = {x:1 for x in a}
    ans = []
    while s:
        t = s[0]
        ans.append(t)
        s.pop(0)
        cur = t
        while cur <= k:
            if cur not in u:
                print(-1)
                continue
            import bisect
            idx = bisect.bisect_left(s, cur)
            if idx < len(s) and s[idx] == cur:
                s.pop(idx)

            cur += t

    print(len(ans))
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int, input().split()))
    cnt = Counter([x % m for x in a])
    ans = 0
    for x in list(cnt.keys()):
        if cnt[x] == 0:
            continue

        if x == 0 or (m % 2 == 0 and x == m // 2):
            ans += 1
            cnt[x] = 0
        else:
            y = m - x
            c1, c2 = cnt[x], cnt.get(y, 0)
            if c2 == 0:
                ans += c1
            else:
                ans += 1 + max(0, abs(c1 - c2) - 1)
            cnt[x] = 0
            cnt[y] = 0

    print(ans)
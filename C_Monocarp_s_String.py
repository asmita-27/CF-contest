from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s =  input().strip()

    cur = s.count('a') - s.count('b')
    lst = {0: -1}
    pr = 0
    ans = n

    for i in range(n):
        pr += 1 if s[i] == 'a' else -1
        lst[pr] = i
        if (pr - cur) in lst:
            ans = min(ans, i - lst[pr - cur])

    print(-1 if ans == n else ans)
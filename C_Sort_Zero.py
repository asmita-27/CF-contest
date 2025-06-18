from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n = int(input())
    a = list(map(int,input().split()))
    cnt = Counter(a)
    ans = 0
    for i in a:
        a.sort()
        if i in cnt and cnt[i]>=1:
            ans += 1
            a.remove(i)

    print(ans)

from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    sm = sum(a)
    x = s - sm

    if x == 0:
        print(-1)
    elif x < 0:
        print(*a)
    else:
        if x == 1:
            cnt = [0,0,0]
            for x in a:
                cnt[x] += 1 
            ans = [0]*cnt[0] + [2]*cnt[2] + [1]*cnt[1]
            print(*ans)
        else:
            print(-1)
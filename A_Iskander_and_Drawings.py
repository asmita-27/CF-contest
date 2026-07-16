from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input()
    ans, cnt = 0, 0
    for i in s:
        if i=="*":
            cnt = 0
        else:
            cnt += 1
        ans = max(ans, (cnt+1)//2)
    print(ans)


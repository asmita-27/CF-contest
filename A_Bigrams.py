from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for x in a:
        if x >= 2:
            cnt += 1
    if max(a) >= 3:
        print("YES")
    elif cnt >= 2:
        print("YES")
    else:
        print("NO")
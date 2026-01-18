from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0] * (n + 1)
    for x in a:
        cnt[x] += 1

    if cnt[0] == 0:
        print("NO")
    elif cnt[1] > 0:
        print("YES")
    else:
        print("YES" if cnt[0] == 1 else "NO")
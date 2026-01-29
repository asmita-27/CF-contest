from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    if a == b:
        print(-1)
        continue

    ans = 0
    for i in range(n):
        if a[i] != b[i]:
            ans = max(ans, abs(a[i] - b[i]))

    print(ans)
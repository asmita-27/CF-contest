from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    i = n - 1
    while i >= 0:
        ans += a[i]
        i -= 2
    print(ans)
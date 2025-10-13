from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += a[i]
    ans = 0
    pref = 0
    for i in range(n - 1):
        pref += a[i]
        ans = max(ans, math.gcd(pref, s - pref))
    print(ans)
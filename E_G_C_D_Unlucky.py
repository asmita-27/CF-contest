from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))

    a = [0] * n
    for i in range(n):
        g = math.gcd(p[i], s[i])
        a[i] = (p[i] // g) * s[i]

    cur = 0
    ok = True
    for i in range(n):
        cur = math.gcd(cur, a[i])
        if cur != p[i]:
            ok = False
            break

    cur = 0
    for i in range(n-1, -1, -1):
        cur = math.gcd(cur, a[i])
        if cur != s[i]:
            ok = False
            break

    print("YES" if ok else "NO")
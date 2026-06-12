from collections import defaultdict, Counter, deque
import os
import math
import sys

MOD = 10**9 + 7
mx = 500000

spf = list(range(mx + 1))
for i in range(2, int(mx ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, mx + 1, i):
            if spf[j] == j:
                spf[j] = i
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    prm = {}
    for num in a:
        while num > 1:
            p = spf[num]
            cnt = 0
            while num % p == 0:
                num //= p
                cnt += 1
            prm[p] = prm.get(p, 0) + cnt
    ans = 1
    for s in prm.values():
        ans = ans * (s + 1) % MOD
    print(ans)
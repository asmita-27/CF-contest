from collections import defaultdict, Counter, deque
import os
import math
import sys


MOD = 998244353

def zro(m):
    if m < 0:
        return 0
    return (m + 1) // 4 + 1
def one(m):
    if m < 1:
        return 0
    return (m + 3) // 4
for _ in range(int(input())):
    n, x = map(int, input().split())

    l0 = zro(x - 1)
    l1 = one(x - 1)

    r0 = zro(n) - l0
    r1 = one(n) - l1

    ans = (l0 * r0 + l1 * r1) % MOD
    print(ans)
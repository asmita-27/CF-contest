from collections import defaultdict, Counter, deque
import os
import math
import sys

MOD = 998244353

def solve_case(a, b):
    n = len(a)
    v0, v1 = 1, 1
    for i in range(1, n):
        M00 = 1 if (a[i-1] <= a[i] and b[i-1] <= b[i]) else 0
        M01 = 1 if (a[i-1] <= b[i] and b[i-1] <= a[i]) else 0
        M10 = 1 if (b[i-1] <= a[i] and a[i-1] <= b[i]) else 0
        M11 = 1 if (b[i-1] <= b[i] and a[i-1] <= a[i]) else 0

        nv0 = (v0 * M00 + v1 * M10) % MOD
        nv1 = (v0 * M01 + v1 * M11) % MOD
        v0, v1 = nv0, nv1

    return (v0 + v1) % MOD
import sys
input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve_case(a, b))

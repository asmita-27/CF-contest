from collections import defaultdict, Counter, deque
import os
import math
import sys

MOD = 998244353
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    blocks = []
    start = 0
    max_a, max_b = a[0], b[0]

    for i in range(n):
        max_a = max(max_a, a[i])
        max_b = max(max_b, b[i])

        # If next element breaks order, close block
        if i == n-1 or (min(a[i+1], b[i+1]) < max_a or min(a[i+1], b[i+1]) < max_b):
            blocks.append(i - start + 1)
            start = i+1
            if start < n:
                max_a, max_b = a[start], b[start]

    ans = 1
    for length in blocks:
        ans = ans * pow(2, length, MOD) % MOD

    print(ans)

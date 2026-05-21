from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0

    for l in range(n):
        needA = 1
        needB = 1
        ok = True

        for r in range(l, n):
            wa = 0
            wb = 0

            if a[r] == needA:
                wa = a[r]
                needA += 1

            if b[r] == needB:
                wb = b[r]
                needB += 1

            if wa != wb:
                ok = False

            if ok:
                ans += 1
            else:
                break

    print(ans)
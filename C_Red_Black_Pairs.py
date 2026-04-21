from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    t = input().strip()
    b = input().strip()

    if n == 1:
        print(int(t[0] != b[0]))
        continue

    dp2 = 0
    dp1 = int(t[0] != b[0])
    for i in range(2, n + 1):
        one = int(t[i - 1] != b[i - 1])
        two = int(t[i - 2] != t[i - 1]) + int(b[i - 2] != b[i - 1])

        cur = min(dp1 + one, dp2 + two)

        dp2, dp1 = dp1, cur

    print(dp1)
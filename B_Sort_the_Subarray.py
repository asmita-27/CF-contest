from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l = 0
    r = n - 1

    while l < n and a[l] == b[l]:
        l += 1

    while r >= 0 and a[r] == b[r]:
        r -= 1

    while l > 0 and b[l - 1] <= b[l]:
        l -= 1

    while r + 1 < n and b[r] <= b[r + 1]:
        r += 1

    print(l + 1, r + 1)



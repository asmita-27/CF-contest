from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):

    n, x = map(int, input().split())
    a = [0] * 100000
    s = 0
    for _ in range(3):
        a = list(map(int, input().split()))
        for j in range(n):
            if (x | a[j]) != x:
                break
            s |= a[j]
    print("YES" if s == x else "NO")



from collections import defaultdict, Counter, deque
import os
import math
import sys

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    p = [-1] * n
    for i in range(1, n):
        p[i] = p[i - 1]
        if a[i] != a[i - 1]:
            p[i] = i - 1
    for i in range(int(input())):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        if p[r] < l:
            print("-1 -1")
        else:
            print(p[r] + 1, r + 1)
    if _ + 1 != t:
        print()
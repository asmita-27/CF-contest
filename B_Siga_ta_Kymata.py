from collections import defaultdict, Counter, deque
import os
import math
import sys

 
def solve():
    n = int(input())
    p = list(map(int, input().split()))
    s = input()
 
    mn = 0
    mx = 0
    for i in range(n):
        if p[i] < p[mn]:
            mn = i
        if p[i] > p[mx]:
            mx = i

    if s[0] == "1" or s[-1] == "1":
        print(-1)
        return

    if s[mn] == "1" or s[mx] == "1":
        print(-1)
        return
 
    print(5)
    print(1, mn + 1)
    print(1, mx + 1)
    print(mn + 1, n)
    print(mx + 1, n)
    print(min(mn + 1, mx + 1), max(mn + 1, mx + 1))
 
 
for _ in range(int(input())):
    solve()
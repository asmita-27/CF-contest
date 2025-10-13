from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    diff = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[n - 1 - i][n - 1 - j]:
                diff += 1
    diff //= 2  
    if diff > k:
        print("NO")
    else:
        k -= diff
        if n % 2 == 1:
            print("YES")
        elif k % 2 == 1:
            print("NO")
        else:
            print("YES")
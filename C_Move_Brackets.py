from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n=  int(input())
    s = input().strip()

    ans = 0
    bal = 0

    for ch in s:
        if ch == '(':
            bal += 1
        else:
            bal -= 1
            if bal < 0:
                bal = 0
                ans += 1

    print(ans)

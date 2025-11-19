from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))

    sum_even = 0
    sum_odd = 0
    seen = set()
    seen.add(0)  
    flag = False

    for i in range(n):
        if i % 2 == 0:
            sum_even += v[i]
        else:
            sum_odd += v[i]

        diff = sum_odd - sum_even

        if diff in seen:
            flag = True
            break
        seen.add(diff)

    print("YES" if flag else "NO")

from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))

    smEvn = 0
    smOdd = 0
    seen = set()
    seen.add(0)  
    flag = False

    for i in range(n):
        if i % 2 == 0:
            smEvn += v[i]
        else:
            smOdd += v[i]

        diff = smOdd - smEvn

        if diff in seen:
            flag = True
            break
        seen.add(diff)

    print("YES" if flag else "NO")

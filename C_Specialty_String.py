from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    stk = []
    for c in s:
        if stk and stk[-1] == c:
            stk.pop()
        else:
            stk.append(c)
    print("YES" if not stk else "NO")
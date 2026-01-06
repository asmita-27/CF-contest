from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s , t = input().strip().split()
    
    cntS = Counter(s)
    cntT = Counter(t)
    if cntS == cntT:
        print("YES")
    else:
        print("NO")
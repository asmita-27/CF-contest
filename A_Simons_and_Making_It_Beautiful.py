from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    
    mx = p.index(n)  
    p[0], p[mx] = p[mx], p[0]
    print(*p)
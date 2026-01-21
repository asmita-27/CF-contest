from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a =  list(map(int,input().split()))
    b = []
    
    t = min(a)+max(a)
    for i in a:
        b.append(t - i)
    print(*b)
    
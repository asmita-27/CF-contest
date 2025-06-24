from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    a,x,y = map(int, input().split())
    if x>y:
        x,y = y,x
    if a<x:
        print("YES")
    elif a>y:
        print("YES")
    else:
        print("NO")


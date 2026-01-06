from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    if a==b==c==d:
        print("YES")
    else:
        print("NO")
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    # n = int(input())
    x,y = map(int,input().split())
    if (x==y) or (y==1) or (x==y+1):
        print(-1)
    elif x<y:
        print(2)
    else:
        print(3)
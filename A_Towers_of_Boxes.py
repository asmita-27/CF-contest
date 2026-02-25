from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,m,d = map(int,input().split())
    mx = d//m+1
    tow = (n+mx-1)//mx
    print(tow)
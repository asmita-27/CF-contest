from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # def avg(x):
    #     return math.floor(sum(x)/ len(x))
    # av = avg(a)
    # print(max(a)-av)
    mn , mx = min(a), max(a)
    print((mx - mn+1)//2)
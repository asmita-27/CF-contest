from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    maxx =  a[-1]- a[0]
    first = abs(k-a[0])
    last = abs(k-a[-1])
    print(min(maxx+first, maxx+last)) 
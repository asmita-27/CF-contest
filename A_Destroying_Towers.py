from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mn = float('inf')
    res=0 
    for i in a :
        mn  = min(mn, i)
        res += mn
    print(res)
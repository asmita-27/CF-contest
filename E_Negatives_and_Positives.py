from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    neg, tot = 0,0
    minn = min(abs(i) for i in a)
    for i in a :
        if i<= 0:
            neg += 1
        tot += abs(i)
    
    if neg%2==0:
        print(tot)
    else:
        print(tot - 2*minn)
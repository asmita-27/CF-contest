from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n , a= map(int, input().split())
    v= list(map(int, input().split()))
    l,r = 0,0
    for i in v:
        if a>i:
            l+=1
        if a<i:
            r+=1
    print(a-1 if l>r else a+1)
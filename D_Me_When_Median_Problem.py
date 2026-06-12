from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l, r = 0, 10**9 + 5
    while l<r:
        md = (l+r)//2
        o,z,pre = 0,0,-1
        for i in range(n):
            typ = 0
            if a[i]>=md:
                typ+=1
            if b[i]>=md:
                typ +=1
            if typ ==1:
                continue
            if typ==2:
                o+=1
                pre =1
            if typ==0:
                if pre!=0:
                    z+=1
                pre =0 
        if o>z:
            l= md+1
        else:
            r = md 
    print(l-1)
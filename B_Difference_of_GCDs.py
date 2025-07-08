from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,l,r = map(int, input().split())
    
    # if n==1:
    #     print("YES")
    #     print(l)
    #     continue
    
    # if n> (l-r):
    #     print("NO")
    #     continue
    
    flg = 1
    a = [0]*(n+1)
    for i in range(1,n+1):
        a[i]= ((l-1)//i+1)* i
        if a[i] > r:
            flg = 0
    
    if flg:
        print("YES")
        print(" ".join(map(str, a[1:])))
    else:
        print("NO")
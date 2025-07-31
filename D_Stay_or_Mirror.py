from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    x=0
    inv1=[0]*n
    inv2=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if p[i]>p[j]:
                x+=1
                inv2[i]+=1
                inv1[j]+=1
    ans=x
    for i in range(n):
        Ai=(n-1-i - inv2[i]) - inv1[i]
        if Ai<0:
            ans+=Ai
    print(ans, ) 
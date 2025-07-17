from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int, input().split())
    cas = []
    for  _ in range(n):
        l,r,real = map(int, input().split())
        cas.append((l, r, real))
    vis = [0]*n
    curr = k
    while True:
        best  =-1
        bestIndex = -1
        
        for i in range(n):
            if not vis[i]:
                l,r,real = cas[i]
                if l<=curr<=r:
                    if real>best:
                        best = real
                        bestIndex = i
        if bestIndex == -1:
            break
        
        vis[bestIndex] = 1
        curr = best
    print(curr)
    

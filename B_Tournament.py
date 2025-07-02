from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,j,k = map(int, input().split())
    a = list(map(int, input().split()))
    maxx = max(a)
    if k>1  :
        print("YES")
        continue
    if k== 1:
        if maxx == a[j-1]:
            print("YES")
        else:
            print("NO")
    


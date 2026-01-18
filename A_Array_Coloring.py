from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    cnt = 0
    for i in range(n):
        cnt += (a[i]%2!= (i+1)%2)
    if cnt ==0 or cnt ==n:
        print("YES")
    else:
        print("NO")
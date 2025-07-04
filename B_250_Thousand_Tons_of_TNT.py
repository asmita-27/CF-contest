from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
  
    ans = -1
    for i in range(1,n+1):
        if n%i == 0:
            mx = float('-inf')
            mn = float('inf')
            for j in range(0,n,i):
                summ = sum(a[j:j+i])
                mx = max(mx, summ)
                mn = min(mn, summ) 
            ans = max(ans, mx - mn)
                
    print(ans)
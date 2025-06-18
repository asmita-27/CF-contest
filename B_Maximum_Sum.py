from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    pre = [0] * (n + 1)
 
    for i in range(n):
        pre[i + 1] = pre[i] + a[i]
 
    ans =0 
    
    for i in range(k + 1):
        ans = max(ans, pre[n-(k-i)] - pre[2*i])
 
    print(ans)
 
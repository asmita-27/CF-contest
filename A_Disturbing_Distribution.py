from collections import defaultdict, Counter, deque
import os
import math
import sys
MOD = 676767677
 

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if a[i]>1:
            res+=a[i]
    if a[-1]==1:
        res+=1
    print(res%MOD)
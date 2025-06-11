from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    i,j = n-1, n-1
    while i >  0 and j >  0:
        if math.gcd(a[i], a[j]) == 1:
            res = max(res, i+j+2)
            j -= 1
            i -= 1
         
 
    print(res if res > 0 else -1)
            
from collections import defaultdict, Counter, deque
import os
import math
import sys

 
n = int(input())
x = list(map(int, input().split()))
q = int(input())
x.sort()
for _ in range(q):
    m = int(input())
    l, r = 0, n-1
    ans = 0
    while l<=r:
        mid =  (l+r)//2
        if x[mid]<= m:
            ans += mid - l + 1
            l = mid + 1
        else:
            r = mid - 1
        
    print(ans)
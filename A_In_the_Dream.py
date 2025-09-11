from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    
    r1,k1,r2,k2 = a,b,c-a,d-b
    
    def valid(r, k):
        return max(r, k) <= 2 * min(r, k) + 2

    if valid(r1, k1) and valid(r2, k2):
        print("YES")
    else:
        print("NO")



from collections import defaultdict, Counter, deque
import os
import math
import sys



n,k = map(int, input().split())
h = list(map(int, input().split()))
ans = float('inf')
i =0
while i < n-2:
    ans = min(ans, (h[i]+ h[i+1] + h[i+2]) )
    i += 1
    
print((ans-i if ans != float('inf') else -1) )
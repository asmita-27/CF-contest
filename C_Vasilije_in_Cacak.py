from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
  
    n, k,x = map(int, input().split())   
 
    minn = k * (k + 1) // 2
    maxx = n * (n + 1) // 2 - (n - k) * (n - k + 1) // 2

    if 2 * x >= minn and 2 * x <= maxx:
        print("YES")
    else:
        print("NO")
 
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n,k = map(int, input().split())
    
    if n % 2 == k%2 and n >= k * k:
        print("YES")
    else:
        print("NO")
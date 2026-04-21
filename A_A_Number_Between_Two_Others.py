from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    x, y = map(int, input().split())
    
    if y == 2 * x:
        print("NO")
    else:
        print("YES")
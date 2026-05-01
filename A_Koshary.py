from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    x,y = map(int,input().split())
    
    if x%2==0 or y%2==0:
        print("YES")
    else:
        print("NO")
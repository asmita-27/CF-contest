from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    if 67 in a:
        print("YES")
    else:
        print("NO")
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.remove(max(a))
    
    sm = 0
    for i in range(n-2):
        sm += abs(a[i]-a[i+1])
        
    print(sm)
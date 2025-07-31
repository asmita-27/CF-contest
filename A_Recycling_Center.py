from collections import defaultdict, Counter, deque
import os
import math
import sys
    
for i in range(int(input())):
    n,c = map(int, input().split())
    a = list(map(int, input().split()))
    deadlines = []
    for weight in a:
        if weight > c:
            deadlines.append(-1)
        else:
            x = c // weight
            deadlines.append(x.bit_length() - 1)  
    deadlines.sort()
    
    free = 0
    for d in deadlines:
        if d >= free:
            free += 1
    print(n - free)
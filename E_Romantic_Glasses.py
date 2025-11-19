from collections import defaultdict, Counter, deque
import os
import math
import sys

for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    
    s = set()
    k = 4
    s.add(k)
    
    p = 0
    temp = 1

    found = False

    for x in v:   
        p += x * temp
        temp = -temp

        if (p ^ k) in s:
            print("YES")
            found = True
            break
        s.add(p ^ k)

    if not found:
        print("NO")

from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    segments = []
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        segments.append((a, b))
    
    segments.sort()
    valid = True
    seen = set()
    for a, b in segments:
        if b in seen:
            valid = False
            break
        seen.add(b)

    print("YES" if valid else "NO")

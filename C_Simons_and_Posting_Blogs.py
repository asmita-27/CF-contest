from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    blogs = [list(map(int, input().split()))[1:] for _ in range(n)]
    
    seen = set()
    ans = []
    
    for i in range(n-1, -1, -1):
        for user in reversed(blogs[i]):   # <-- FIX HERE
            if user not in seen:
                seen.add(user)
                ans.append(user)
    
    print(*ans)
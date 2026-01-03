from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    ans = 0
    for i in range(n):
        if s[i] != s[n-1]:
            ans += 1
        
    print(ans)
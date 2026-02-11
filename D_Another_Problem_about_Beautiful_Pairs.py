from collections import defaultdict, Counter, deque
import os
import math
import sys



for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    ans = 0
    
    for i in range(1, n + 1):
        ai = a[i] 
        j = i + ai
        
        while j <= n:
            if a[j] * ai == j - i:
                ans += 1
            j += ai
    
    print(ans)
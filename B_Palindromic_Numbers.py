from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):

    n = int(input())
    s = input()
    
    if s[0] != '9': 
        ans = ''.join(str(9 - int(ch)) for ch in s)
    else: 
        t = '1' * (n + 1)
        x = int(t) - int(s)
        ans = str(x).zfill(n)  
    print(ans)
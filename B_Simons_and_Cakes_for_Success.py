from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    ans = 1
    d = 2
    while d*d <= n:
        if n % d == 0:
            ans *= d
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ans *= n
    
    print(ans)
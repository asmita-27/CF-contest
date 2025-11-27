from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    ans = []
    
    for i in range(n):
        if i == 0 or i == n - 1:
            ans.append(p[i])
        else:
            if (p[i-1] < p[i]) != (p[i] < p[i+1]):
                ans.append(p[i])
    
    print(len(ans))
    print(*ans)
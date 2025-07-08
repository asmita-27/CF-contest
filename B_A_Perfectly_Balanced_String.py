from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s = input().strip()
    
    mp = Counter(s)
    
    # if max(mp.values()) - min(mp.values()) > 1:
    #     print("NO")
    #     continue
    # else:
    #     print("YES")

    
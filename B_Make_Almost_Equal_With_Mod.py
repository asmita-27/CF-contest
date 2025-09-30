from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    found = False
    for j in range(1, 61):  
        k = 1 << j
        rem = {x % k for x in a}
        if len(rem) == 2:
            print(k)
            found = True
            break 

    # if not found:
    #     print(10**18)
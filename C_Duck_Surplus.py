from collections import defaultdict, Counter, deque
import os
import math
import sys
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cur = a[0]
    for x in a[1:]:
        if x < cur:
            cur += x
        else:
            cur = x
    print(cur)
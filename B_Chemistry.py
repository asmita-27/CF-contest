from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n, k = map(int, input().split())
    s = input()
    freq = Counter(s)
    cnt = 0
    for i in freq.values():
        if i % 2 != 0:
            cnt +=1 

     
    if cnt <= k + 1:
        print("YES")
    else:
        print("NO")

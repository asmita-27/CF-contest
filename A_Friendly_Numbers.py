from collections import defaultdict, Counter, deque
import os
import math
import sys

def digSm(n):
    return sum(int(d) for d in str(n))
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n , n+91):
        if i-digSm(i)==n:
            cnt+=1
    print(cnt)
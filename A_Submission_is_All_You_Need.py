from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
 
    n = int(input())
    a = list(map(int, input().split()))
    tot = 0
    for x in a:
        if x == 0:
            tot += 1
        else:
            tot += x
    print(tot)
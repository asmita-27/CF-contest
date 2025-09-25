from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    neg = a.count(-1)
    zero = a.count(0)
    
    ops = zero
    if neg % 2 == 1:
        ops += 2
    print(ops)
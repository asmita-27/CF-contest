from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n = int(input())
    s = input()
    sSrt = ''.join(sorted(s))
    diff = sum(1 for i in range(len(s)) if s[i] != sSrt[i])
    print(diff//2)

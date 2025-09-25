from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    freq = Counter(a) 
    ms = sum(1 for i in range(k) if freq.get(i, 0) == 0)
    cnt_k = freq.get(k, 0)
    print(max(ms, cnt_k))
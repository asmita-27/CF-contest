from collections import defaultdict, Counter, deque
import os
import math
import sys


n,k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))
for c in range(k):
    p = a.index(q[c])
    print(p + 1, end=' ')
    a = [a[p]] + a[:p] + a[p+1:]
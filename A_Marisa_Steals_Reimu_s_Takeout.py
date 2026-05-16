from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    c0 = w.count(0)
    c1 = w.count(1)
    c2 = w.count(2)
    pairs = min(c1, c2)
    c1 -= pairs
    c2 -= pairs
    ans = c0 + pairs + c1 // 3 + c2 // 3

    print(ans)
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)

    o = 0
    e = 0
    for cnt in freq.values():
        if cnt & 1:
            o += 1
        else:
            e += 1

    ans = o + 2 * e

    if o == 0 and (e % 2) != (n % 2):
        ans -= 2

    print(ans)
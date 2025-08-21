from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n =  int(input())
    ans = []
    k = 1
    while 10**k + 1 <= n:
        d = 10**k + 1
        if n % d == 0:
            ans.append(n // d)
        k += 1

    if ans :
        print(len(ans))
        ans.sort()
        print(*ans)
    else:
        print(0)
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a, n = map(int, input().split())
    d = input().split()

    x, y = d[0], d[1]

    l = len(str(a))
    ans = float('inf')
    for lng in range(max(1, l - 1), l + 2):
        tot = 1 << lng
        for msk in range(tot):
            s = []
            for i in range(lng):
                if (msk >> i) & 1:
                    s.append(y)
                else:
                    s.append(x)
            if lng > 1 and s[0] == '0':
                continue
            num = int("".join(s))
            ans = min(ans, abs(a - num))

    print(ans)
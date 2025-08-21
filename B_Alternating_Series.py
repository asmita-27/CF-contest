from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())

    ans = []
    for i in range(n):
        if i % 2 == 0:
            ans.append(-1)
        else:
            if i == n - 1:
                ans.append(2)
            else:
                ans.append(3)
    print(*ans)
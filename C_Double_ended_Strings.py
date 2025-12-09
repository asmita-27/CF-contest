from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a = input().strip()
    b = input().strip()
    n,m = len(a), len(b)
    ans = 0

    for length in range(1, min(n, m) + 1):
        for i in range(n - length + 1):
            for j in range(m - length + 1):
                if a[i:i+length] == b[j:j+length]:
                    ans = max(ans, length)

    print(n + m - 2 * ans)

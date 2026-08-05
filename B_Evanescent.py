from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    x = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            x += 1
    ans = x
    for i in range(1, n - 1):
        cur = x
        if s[i] != s[i - 1]:
            cur -= 1
        if s[i] != s[i + 1]:
            cur -= 1
        if s[i - 1] != s[i + 1]:
            cur += 1
        ans = min(ans, cur)
    print(ans)
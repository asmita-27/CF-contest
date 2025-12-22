from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    s = s + s
    ans = 1
    cnt = 1
    zero = False

    for i in range(2 * n - 1):
        if s[i] == '0' and s[i + 1] == '0':
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 1

        if s[i] == '0':
            zero = True

    if zero:
        print(ans)
    else:
        print(0)





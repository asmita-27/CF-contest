from collections import defaultdict, Counter, deque
import os
import math
import sys


n = int(input())
s = input().strip()

for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        print("YES")
        print(i, i + 1)
        break
else:
    print("NO")
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    ans = 0
    if "2026" not in s and "2025" in s:
        ans =1 
    print(ans)
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    ans = 1
    if n==2:
        ans = 9
    elif n== 3 or n==4:
        ans = 4*n*n-n-4
    elif n>4:
        ans = 5*n*n-5*n-5
    print(ans)
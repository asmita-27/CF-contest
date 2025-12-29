from collections import defaultdict, Counter, deque
import os
import math
import sys

n = int(input())
ans = 0
k = n // 2
if n % 2 == 0:
    ans = (k+1)*(k+1)
else:
    ans = 2*(k+1)*(k+2)
print(ans)
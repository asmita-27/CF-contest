from collections import defaultdict, Counter, deque
import os
import math
import sys

MOD = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    print(((((n*(n+1))%MOD)*(4*n-1))%MOD*337)%MOD)
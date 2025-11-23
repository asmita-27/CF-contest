from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    used = set()

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and i not in used:
            used.add(i)
            n //= i
            break
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and i not in used:
            used.add(i)
            n //= i
            break
    if len(used) < 2 or n in used or n == 1:
        print("NO")
    else:
        print("YES")
        used.add(n)
        print(*used)
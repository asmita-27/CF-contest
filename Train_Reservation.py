from collections import defaultdict, Counter, deque
import os
import math
import sys


# for _ in range(int(input())):
#     pass

n, x = input().split()
n = int(n)
y = ord(x) - ord('A')   
for _ in range(n):
    s = input().strip()
    if s[y] == 'o':
        print("Yes")
        break
else:
    print("No")
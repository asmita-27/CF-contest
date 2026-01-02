from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    if n%2==1:
        print(0)
    else:
        print(n//4+1)

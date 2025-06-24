from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    a,b,c= map(int, input().split())
    
    print("1" + "0" * (a - 1), "1" * (b - c + 1) + "0" * (c - 1))


from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a,b,n = map(int, input().split())
    
    if b*n<= a or  b>=a:
        print(1)
    else:
        print(2)
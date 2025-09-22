from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input()) 
    for i in range(n, 0, -1):
        print(i, end=' ')
    print(n, end=' ')
    for i in range(1, n):
        print(i, end=' ')
    
    print()  
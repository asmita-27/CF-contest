from collections import defaultdict, Counter, deque
import os
import math
import sys

for _ in range(int(input())):
    n = int(input())
    print(2 * n)
    for i in range(1, n + 1):
        if i == 1:
            continue  
        print(i, 1, n) 
        print(i, 2, n)
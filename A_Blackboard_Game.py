from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    if n%4 == 0:
        print("Bob")
    else:
        print("Alice")
    
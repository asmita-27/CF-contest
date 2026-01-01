from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    y,r = map(int, input().split())
    print(min(n, r+y//2))
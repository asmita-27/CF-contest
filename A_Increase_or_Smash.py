from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split ()))
    set_a = set(a) 
    print(len(set_a)*2-1)
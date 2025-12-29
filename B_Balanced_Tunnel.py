from collections import defaultdict, Counter, deque
import os
import math
import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos = [0]* n
for i in range(n):
    pos[b[i]]= i

c = [0]* n
for i in range(n):
    c[i]= pos[a[i]]

mx = -1
ans =0
for 
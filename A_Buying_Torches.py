from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    x,y , k = map(int, input().split())
    stkGain = x-1
    stkNeed = k*y+k-1
    trd = (stkNeed+stkGain-1 )// stkGain
    trd+=k
    print(trd)
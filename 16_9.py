from collections import defaultdict, Counter, deque
import os
import math
import sys


x,y = map(int,input().split())
if x%16==0 and y%9==0:
    print("Yes")
else:
    print("No")

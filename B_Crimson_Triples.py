from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    res =0 
    for i in range(1,n):
        cnt =  n//i
        res +=  cnt*cnt  
    print(res+1)
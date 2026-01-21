from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    b,a = map(int, input().split())
    ans = -1
    if (a+b)&1 ==0:
        ans = (a+b)
    if a%2==1 and b%2==1:
        ans =  max(ans, a*b+1)
    elif a%2==0 and (a%4==0 or b%2==0):
        ans = max(ans, 2+a*b //2)
    print(ans)
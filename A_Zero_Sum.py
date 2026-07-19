from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2==1:
        print("NO")
    else:
        cnt1 = a.count(1)
        if cnt1 % 2 == (n // 2) % 2:
            print("YES")
        else:
            print("NO")
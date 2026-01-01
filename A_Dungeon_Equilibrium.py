from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n =  int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)
    cnt = 0
    for i in freq :
        if freq[i]>= i:
            cnt += (abs(freq[i]-i))
        else:
            cnt += freq[i]
    print(cnt)
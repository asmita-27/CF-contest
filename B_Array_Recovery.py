from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a =  (map(int, input().split()))
    ans = [0]
    for i in a:
        if i!=0 and ans[-1]-i>=0:
            print(-1)
            break
        else:
            ans.append(ans[-1] + i)
    else:
        print(*ans[1:])

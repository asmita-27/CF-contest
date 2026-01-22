from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    nums = set()
 
    for k in range(2, 1001):
        val = 1 + k
        p = k * k
        for cnt in range(2, 21):
            val += p
            if val > 10**6:
                break
            nums.add(val)
            p *= k
    if n in nums:
        print("YES")
    else:
        print("NO")
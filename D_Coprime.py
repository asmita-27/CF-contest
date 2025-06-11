from collections import defaultdict, Counter, deque
import os
import math
import sys

  
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    pos = {} 
    for id, val in enumerate(a):
        pos[val] = id
    res = -1
    nums = list(pos.keys())

    for i in range(len(nums)):
        for j in range(len(nums)):
            if math.gcd(nums[i], nums[j]) == 1:
                res = max(res, pos[nums[i]] + pos[nums[j]] + 2)   
    print(res)

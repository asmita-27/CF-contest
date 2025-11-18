from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    ans = n + 1
    
    for c in range(26):
        ch = chr(ord('a') + c)
        l, r = 0, n - 1
        cnt = 0
        
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] == ch:
                cnt += 1
                l += 1
            elif s[r] == ch:
                cnt += 1
                r -= 1
            else:
                cnt = n + 1
                break
        ans = min(ans, cnt)
    
    if ans == n + 1:
        ans = -1
    print(ans)
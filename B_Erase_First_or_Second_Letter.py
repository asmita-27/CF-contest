from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    ans = [0] * n
    nxt = [n] * 26  
    ans[n - 1] = 1
    nxt[ord(s[n - 1]) - ord('a')] = n - 1

    for i in range(n - 2, -1, -1):
        ans[i] = ans[i + 1] + (nxt[ord(s[i]) - ord('a')] - i)
        nxt[ord(s[i]) - ord('a')] = i
    
    print(ans[0])

    
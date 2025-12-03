from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    cnt = [0]*26
    p = [0] *26
    for ch in s:
        cnt[ord(ch)-97] += 1
    ans = 0
    for i in s:
        idx = ord(i)-97
        cnt[idx] -= 1
        p[idx] += 1
        curr = 0
        for j in range(26):
            curr +=  min(1,cnt[j]) + min(1,p[j])
        ans = max(ans, curr)
    print(ans)
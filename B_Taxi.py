from collections import defaultdict, Counter, deque
import os
import math
import sys

n = int(input())
s =  list(map(int, input().split()))

freq = Counter(s)
ans = 0

ans += freq[4]

ans += freq[3]
freq[1] = max(0, freq[1] - freq[3])

ans += (freq[2] + 1) // 2
if freq[2] % 2 == 1:
    freq[1] = max(0, freq[1] - 2)

ans += (freq[1] + 3) // 4

print(ans)


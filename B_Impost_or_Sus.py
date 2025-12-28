from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s = "u" + input() + "u"
    s = list(s)
    ans = 0
    for i in range(1, len(s)):
        if s[i - 1] == 'u' and s[i] == 'u':
            ans += 1
            s[i] = 's'
    print(ans)
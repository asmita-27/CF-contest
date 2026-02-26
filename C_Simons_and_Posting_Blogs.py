from collections import defaultdict, Counter, deque
import os
import math
import heapq
import sys
 

for _ in range(int(input())):
    n = int(input())
    blog = [list(map(int, input().split()))[1:] for _ in range(n)]
    res = []
    for a in blog:
        seen = set()
        tmp = []
        for x in reversed(a):
            if x not in seen:
                seen.add(x)
                tmp.append(x)
        res.append(tmp[:])
    heap = []
    for i, rev in enumerate(res):
        if rev:
            heapq.heappush(heap, (tuple(rev), i))
    used = set()
    ans = []
    while heap:
        key, i = heapq.heappop(heap)
        cur = tuple(x for x in res[i] if x not in used)
        if not cur:
            continue
        if cur != key:
            heapq.heappush(heap, (cur, i))
            continue
        for x in cur:
            if x not in used:
                used.add(x)
                ans.append(x)
    print(*ans)
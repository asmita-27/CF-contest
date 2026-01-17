import sys
from collections import deque

input = sys.stdin.buffer.readline

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * (n + 1)

q = deque([1])
color[1] = 0

c0 = 1
c1 = 0

while q:
    u = q.popleft()
    cu = color[u]
    for v in adj[u]:
        if color[v] == -1:
            color[v] = 1 - cu
            if color[v] == 0:
                c0 += 1
            else:
                c1 += 1
            q.append(v)

print(c0 * c1 - (n - 1))

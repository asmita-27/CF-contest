import sys
from collections import deque

input = sys.stdin.buffer.readline

def find_leaf(start, forbid, adj, deg):
    # BFS/DFS from start avoiding 'forbid' until we find a node with global deg == 1
    stack = [start]
    visited = set([forbid])  # mark forbid as visited so we never go into it
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        if deg[v] == 1:
            return v
        for w in adj[v]:
            if w not in visited:
                stack.append(w)
    return None

t = int(input().strip())
out_lines = []
for _ in range(t):
    n = int(input().strip())
    adj = [[] for _ in range(n+1)]
    deg = [0]*(n+1)
    for _e in range(n-1):
        u,v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1

    # if already a path (all degrees <= 2)
    bad = -1
    for i in range(1, n+1):
        if deg[i] > 2:
            bad = i
            break
    if bad == -1:
        out_lines.append("-1")
        continue

    b = bad
    # find leaves in at least two different neighbor-branches of b
    leaves = []
    for nb in adj[b]:
        leaf = find_leaf(nb, b, adj, deg)
        if leaf is not None:
            leaves.append(leaf)
        if len(leaves) >= 2:
            break

    # we are guaranteed a solution exists, so we should have two leaves
    a, c = leaves[0], leaves[1]
    out_lines.append(f"{a} {b} {c}")

sys.stdout.write("\n".join(out_lines) + "\n")

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # BFS to compute depths
        depth_count = defaultdict(int)
        visited = [False] * (n + 1)

        q = deque([(1, 0)])
        visited[1] = True

        while q:
            node, d = q.popleft()
            depth_count[d] += 1
            for nxt in adj[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, d + 1))

        max_depth = max(depth_count.keys())
        ans = depth_count[0]  # root alone case

        for d in range(1, max_depth + 1):
            ans = max(ans, depth_count[d] + depth_count[d - 1])

        print(ans)

if __name__ == "__main__":
    solve()

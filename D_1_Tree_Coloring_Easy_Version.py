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

        # BFS to compute depth counts
        depth_count = defaultdict(int)
        visited = [False] * (n + 1)
        q = deque()
        q.append((1, 0))  # (node, depth)
        visited[1] = True

        while q:
            node, depth = q.popleft()
            depth_count[depth] += 1
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append((nei, depth + 1))

        print(max(depth_count.values()))

if __name__ == "__main__":
    solve()

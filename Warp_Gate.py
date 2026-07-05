import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(graph, sources):
    dist = [INF] * (len(graph))
    heap = []
    for node, d in sources:
        dist[node] = d
        heapq.heappush(heap, (d, node))
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v, t = map(int, input().split())
        u -= 1; v -= 1
        graph[u].append((v, t))
        graph[v].append((u, t))

    dist1 = dijkstra(graph, [(0, 0)])
    distB = dijkstra(graph, [(i, X[i]) for i in range(N)])

    A = min(dist1[i] + X[i] for i in range(N))

    for k in range(1, N):
        print(min(dist1[k], A + Y + distB[k]))

solve()

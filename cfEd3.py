from collections import deque

def solve():
    import math
    t = int(input())
    for _ in range(t):
        n, st, en = map(int, input().split()) 
        adj = [[] for _ in range(n+1)]
        for _i in range(n-1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
         
        def find_path(s, t):
            parent = [-1]*(n+1)
            dq = deque()
            dq.append(s)
            parent[s] = s
            while dq:
                cur = dq.popleft()
                if cur == t:
                    break
                for nb in adj[cur]:
                    if parent[nb] == -1:
                        parent[nb] = cur
                        dq.append(nb)
            if parent[t] == -1:
                return [] 
            path = []
            cur = t
            while cur != s:
                path.append(cur)
                cur = parent[cur]
            path.append(s)
            path.reverse()
            return path
         
        P = find_path(st, en)
        setP = set(P) 
        R = [v for v in range(1, n+1) if v not in setP]
         
        if st == en:
            if n % 2 == 0:
                print(-1)
                continue 
            perm = sorted(R) + [st]
        else: 
            if len(R) % 2 == 0:
                order_R = sorted(R)
            else:
                order_R = sorted(R, reverse=True)
            perm = order_R + P
         
        pos = st
        for x in perm:
            if pos == x: 
                pass
            else: 
                parent = [-1]*(n+1)
                dq = deque()
                dq.append(pos)
                parent[pos] = pos
                while dq:
                    cur = dq.popleft()
                    if cur == x:
                        break
                    for nb in adj[cur]:
                        if parent[nb] == -1:
                            parent[nb] = cur
                            dq.append(nb) 
                cur = x
                path_tmp = []
                while cur != pos:
                    path_tmp.append(cur)
                    cur = parent[cur]
                path_tmp.append(pos)
                path_tmp.reverse() 
                pos = path_tmp[1] 
        if pos != en: 
            print(-1)
        else:
            print(" ".join(map(str, perm)))
 
solve()

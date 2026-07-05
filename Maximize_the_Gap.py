import sys
input = sys.stdin.readline

def help(clt, k, d):
    cnt = 0
    lst = -1
    for l, r in clt:
        if lst == -1 or l >= lst + d:
            cnt += 1
            lst = r
            if cnt == k:
                return True
    return False
def solve():
    n,k = map(int, input().split())
    clt = []
    for _ in range(n):
        l, r = map(int, input().split())
        clt.append((l, r))
    clt.sort(key=lambda x: x[1])
    if not help(clt, k, 1):
        print(-1)
        return
    lo, hi = 1, 10**9
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if help(clt, k, mid):
            lo = mid
        else:
            hi = mid - 1
    print(lo)
solve() 

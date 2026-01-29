import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a == sorted(a):
        print(-1)
        continue

    mn = a[-1]
    ans = 10**18

    for i in range(n - 2, -1, -1):
        if a[i] > mn:
            ans = min(ans, a[i] - mn)
        mn = min(mn, a[i])

    print(ans)

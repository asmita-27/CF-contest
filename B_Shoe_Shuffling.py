import sys
input = sys.stdin.readline
 

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    p = list(range(1, n + 1))

    l = 0
    r = 0
    ans = True

    while r < n: 
        while r < n - 1 and s[r] == s[r + 1]:
            r += 1

        if l == r:
            ans = False
        else: 
            p[l:r+1] = [p[r]] + p[l:r]

        l = r + 1
        r += 1

    if ans:
        print(*p)
    else:
        print(-1)

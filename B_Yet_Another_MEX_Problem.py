import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    mp = {}
    for x in arr:
        mp[x] = mp.get(x, 0) + 1

    ans = -1
    for i in range(k):
        if i not in mp:
            ans = i
            break

    if ans == -1:
        print(k - 1)
    else:
        print(ans)

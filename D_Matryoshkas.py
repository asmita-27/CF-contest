import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    res = 0
    last = 0
    prev = -1
    i = 0

    while i < n:
        j = i
        cnt = 0

        while j < n and a[j] == a[i]:
            cnt += 1
            j += 1

        if prev != -1 and a[i] != prev + 1:
            last = 0   
        res += max(0, cnt - last)
        last = cnt
        prev = a[i]
        i = j

    print(res)

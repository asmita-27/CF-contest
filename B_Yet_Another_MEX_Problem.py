import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = [0] * (k + 1)
    miss = set(range(k + 1))

    # first window
    for i in range(k):
        if a[i] <= k:
            freq[a[i]] += 1
            if freq[a[i]] == 1:
                miss.discard(a[i])

    maxMex = (k + 1) if not miss else min(miss)
 
    for i in range(k, n):
        out = a[i - k]
        if out <= k:
            freq[out] -= 1
            if freq[out] == 0:
                miss.add(out)

        inn = a[i]
        if inn <= k:
            freq[inn] += 1
            if freq[inn] == 1:
                miss.discard(inn)

        curMex = (k + 1) if not miss else min(miss)
        maxMex = max(maxMex, curMex)

    print(min(maxMex, k - 1))

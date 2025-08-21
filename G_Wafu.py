import sys
import heapq

MOD = 10**9 + 7
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    heapq.heapify(arr)
    score = 1
    max_contiguous = 0  # all numbers <= this are in the set already

    for _ in range(k):
        # get smallest available number
        while arr and arr[0] <= max_contiguous:
            heapq.heappop(arr)  # skip numbers already in contiguous block

        if not arr:  # only contiguous numbers remain
            # we will remove max_contiguous+1 each time now
            m = max_contiguous + 1
        else:
            m = arr[0]
            heapq.heappop(arr)

        score = (score * m) % MOD

        # after removing m, 1..m-1 will be in the set
        if m - 1 > max_contiguous:
            max_contiguous = m - 1

    print(score % MOD)

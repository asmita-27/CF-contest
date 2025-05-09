
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    m = n - k
    lo = (m - 1) // 2
    hi = k + (m // 2) 
    print(a[hi] - a[lo] + 1)


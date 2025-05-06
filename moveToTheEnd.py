t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pmax = [0] * (n + 1)
    psum = [0] * (n + 1)
    for j in range(n):
        pmax[j + 1] = max(pmax[j], a[j])
        psum[j + 1] = psum[j] + a[j]

    res = []
    for k in range(1, n + 1):
        val = pmax[n - k + 1] + psum[n] - psum[n - k + 1]
        res.append(str(val))
    print(' '.join(res))

import math
for _ in range(int(input())):
    n, k = map(int, input().split())

    d = n.bit_length() - 1
    ans = 0
    for L in range(d):
        need = k - L 
        if need <= 0:
            ans += 1 << L
        elif need > L:
            continue
        else:
            for i in range(need, L + 1):
                ans += math.comb(L, i)
    if k <= d:
        ans += 1

    print(ans)
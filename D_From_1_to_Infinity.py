POW10 = [10**i for i in range(19)]

def sum_digits_0_to_n(n):
    if n <= 9:
        return n * (n + 1) // 2
    res = 0
    while n > 9:
        p = 1
        d = 0
        while p * 10 <= n:
            p *= 10
            d += 1
        msd = n // p
        rem = n % p
        Fpm1 = 0 if d == 0 else d * 45 * POW10[d - 1]
        res += msd * Fpm1
        res += (msd * (msd - 1) // 2) * p
        res += msd * (rem + 1)
        n = rem
    res += n * (n + 1) // 2
    return res

def sum_first_r_digits(x, r):
    return 0 if r == 0 else sum(int(ch) for ch in str(x)[:r])

t = int(input())
for _ in range(t):
    k = int(input())
    N = 0
    rem = k
    r = 0
    for d in range(1, 19):
        cnt = 9 * POW10[d - 1]
        block = cnt * d
        if rem >= block:
            N += cnt
            rem -= block
        else:
            full = rem // d
            N += full
            r = rem - full * d
            break
    ans = sum_digits_0_to_n(N)
    if r:
        ans += sum_first_r_digits(N + 1, r)
    print(ans)

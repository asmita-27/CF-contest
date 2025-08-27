def isPr(x):
    if x < 2: return False
    i = 2
    while i * i <= x:
        if x % i == 0: return False
        i += 1
    return True


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    p = None 
    for pr in range(2, min(k + 2, 50)):
        if isPr(pr) and k % pr != 0:
            p = pr
            break

    inv_k = pow(k % p, p - 2, p)  
    res = []
    for ai in a:
        t_i = (-ai * inv_k) % p
        res.append(ai + t_i * k)

    print(" ".join(map(str, res)))

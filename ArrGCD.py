def sieve(N): 
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, N):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * 2, N, i):
                is_prime[j] = False
    return primes
 
N = 6_000_000
primes = sieve(N)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    suma = 0
    sump = 0
    ans = 0

    for i in range(n):
        suma += a[i]
        sump += primes[i]
        if suma >= sump:
            ans = i + 1

    print(n - ans)


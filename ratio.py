def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [i for i, prime in enumerate(is_prime) if prime]

def main():
    t = int(input())
    test_cases = [int(input()) for _ in range(t)]
    max_n = max(test_cases)

    primes = sieve(max_n)
    
    for n in test_cases:
        total = 0
        for p in primes:
            if p > n:
                break
            total += n // p
        print(total)

if __name__ == "__main__":
    main()

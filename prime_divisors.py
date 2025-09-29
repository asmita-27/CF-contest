import sys
import bisect
 
def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]
 
MAXN = 10**8
primes = sieve(int(MAXN**0.5) + 1)    

prime_divisor_nums = set()
 
prime_divisor_nums.update(primes)
 
for p in primes:
    if p*p <= MAXN:
        prime_divisor_nums.add(p*p)
 
for p in primes:
    if p**4 <= MAXN:
        prime_divisor_nums.add(p**4)
 
for p in primes:
    if p**6 <= MAXN:
        prime_divisor_nums.add(p**6)
 
prime_divisor_nums = sorted(prime_divisor_nums)
  
input_data = sys.stdin.read().split()
t = int(input_data[0])
idx = 1

out = []
for _ in range(t):
    l = int(input_data[idx]); r = int(input_data[idx+1])
    idx += 2
    left = bisect.bisect_left(prime_divisor_nums, l)
    right = bisect.bisect_right(prime_divisor_nums, r)
    out.append(str(right - left))

print("\n".join(out))

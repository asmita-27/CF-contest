def generate_permutation(n):
    if n == 1:
        return "1"
    
    if n % 2 == 0:
        return "-1"
    perm = list(range(1, n + 1)) 
    for i in range(1, n, 2):
        perm[i - 1], perm[i] = perm[i], perm[i - 1]
    return " ".join(map(str, perm))

  
for _ in range(int(input())):
    n = int(input() )
    res  = generate_permutation(n)
    print(res)
 
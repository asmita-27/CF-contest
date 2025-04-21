def solve():
    t = int(input().strip())
    for _ in range(t):
        n, x = map(int, input().split())
        
        if n == 1:
            print(x)
            continue
        p = 1
        while (1 << p) - 1 <= x:
            p += 1
        p -= 1
        m0 = 1 << p 
        m = min(n, m0)
        
        key = list(range(m))
        base = 0
        for num in key:
            base |= num
         
        if base != x:
            missing = x & ~base
            key.append(missing)
         
        while len(key) < n:
            key.append(0)
        
        print(" ".join(str(num) for num in key))

if __name__ == '__main__':
    solve()

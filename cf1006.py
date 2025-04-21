def solve():
    t = int(input().strip())
    for _ in range(t):
        n, k, p = map(int, input().split())
         
        if k == 0:
            print(0)
            continue
        
        abs_k = abs(k) 
        if abs_k > n * p:
            print(-1)
            continue
         
        ops = (abs_k + p - 1) // p
        print(ops)

if __name__ == '__main__':
    solve()

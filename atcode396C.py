def main():
    n, m = map(int, input().split())
    b = list(map(int, input().split()))
    w = list(map(int, input().split()))
    
    b.sort(reverse=True)
    w.sort(reverse=True)
    x = [0] * (n + 1)
    for i in range(1, n + 1):
        x[i] = x[i - 1] + b[i - 1]
    
    bextB = [0] * (n + 1)
    bextB[n] = x[n]
    for i in range(n - 1, -1, -1):
        bextB[i] = max(x[i], bextB[i + 1])
    
    y = [0] * (m + 1)
    for j in range(1, m + 1):
        y[j] = y[j - 1] + w[j - 1]
     
    ans = 0 
    for l in range(0, min(n, m) + 1):
        z = bextB[l] + y[l]
        if z> ans:
            ans = z
    
    print(ans)
 
main()

def solve():
    t = int(input())  
    for _ in range(t):
        n, l, r = map(int, input().split())  
        a = list(map(int, input().split()))  
        
        l -= 1
        r -= 1
        
        subarray = a[l:r+1]
        
        a_sorted = sorted(a)
        a[l:r+1] = a_sorted[l:r+1]
        
        result = sum(a[l:r+1])
        
        print(result)
solve()

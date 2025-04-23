 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
     
    bit_counts = [0] * 30   
    for num in a:
        for b in range(30):
            if (num >> b) & 1:
                bit_counts[b] += 1
    
    max_sum = 0
    for k in range(n):
        curr_sum = 0
        for b in range(30):
            if (a[k] >> b) & 1:
                cnt = n - bit_counts[b]
            else:
                cnt = bit_counts[b]
            curr_sum += cnt * (1 << b)
        max_sum = max(max_sum, curr_sum)
    
    print(max_sum)
 
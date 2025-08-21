MAX_POS = 40  
pow3 = [1] * (MAX_POS + 2)
for i in range(1, MAX_POS + 2):
    pow3[i] = pow3[i-1] * 3
 
cost = [0] * (MAX_POS + 1)
cost[0] = 3
for x in range(1, MAX_POS + 1):
    cost[x] = pow3[x+1] + x * pow3[x-1]

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
 
    cnt = [0] * (MAX_POS + 1)
    m = n
    pos = 0
    while m > 0 and pos <= MAX_POS:
        cnt[pos] = m % 3
        m //= 3
        pos += 1

    D = sum(cnt)  
    if D > k:
        print(-1)
        continue
 
    total_cost = 0
    for i in range(MAX_POS + 1):
        if cnt[i]:
            total_cost += cnt[i] * cost[i]
 
    for x in range(MAX_POS, 0, -1):
        if D >= k:
            break
        if cnt[x] == 0:
            continue
        can_split = (k - D) // 2
        if can_split == 0:
            break
        s = min(cnt[x], can_split)
        cnt[x] -= s
        cnt[x-1] += 3 * s
        D += 2 * s
        total_cost -= s * pow3[x-1]

    print(total_cost)

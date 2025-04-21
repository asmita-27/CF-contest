
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    i = n - 1
    while i >= 0:
        if a[i] > 0:
            pos_sum = 0
            j = i
            while j < n and a[j] > 0:
                pos_sum += a[j]
                j += 1
            dp[i] = pos_sum + dp[j]
        else:
            neg_sum = 0
            j = i
            while j < n and a[j] < 0:
                neg_sum += -a[j]
                j += 1
            dp[i] = neg_sum if neg_sum > dp[j] else dp[j]
        i -= 1
    results.append(str(dp[0]))
print("\n".join(results))

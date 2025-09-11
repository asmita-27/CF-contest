t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input() 
    mxO = 0
    cnt = 0
    for c in s:
        if c == '1':
            cnt += 1
            mxO = max(mxO, cnt)
        else:
            cnt = 0
    if mxO >= k:
        print("NO")
        continue 
    ones = []
    zeros = []
    for i, c in enumerate(s):
        if c == '1':
            ones.append(i)
        else:
            zeros.append(i)
    
    perm = [0] * n
    num = 1
    for i in ones:
        perm[i] = num
        num += 1
    for i in zeros:
        perm[i] = num
        num += 1
    
    print("YES")
    print(' '.join(map(str, perm)))

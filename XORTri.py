t = int(input())
for _ in range(t):
    x = int(input()) 
    if (x & (x - 1)) == 0:
        print(-1)
        continue
 
    m = x.bit_length() - 1 
    if x == (1 << (m + 1)) - 1:
        print(-1)
        continue 
    p = x & -x
 
    q = None
    for j in range(m):
        if ((x >> j) & 1) == 0:
            q = (1 << j)
            break 
    y = p + q
    print(y)

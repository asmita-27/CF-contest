 
 
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    flg = False
    for mask in range(1 << n):
        p = []
        idx = []
        x = []
        for i in range(n):
            if (mask >> i) & 1:
                p.append(s[i])
                idx.append(i + 1)
            else:
                x.append(s[i])
        if p != sorted(p):           
            continue
        x = ''.join(x)
        if x == x[::-1]:              
            print(len(idx))
            if idx:
                print(*idx)
            else:
                print()              
            flg = True
            break
    if not flg:
        print(-1)

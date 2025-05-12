def solve():
    a = input()
    b = input()
    n = len(a)
    m = len(b)

    if m < n or m > 2 * n or a[0] != b[0]:
        print("NO")
        return

    aa = []
    bb = []

    cnt = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            aa.append(cnt)
            cnt = 1
        else:
            cnt += 1
    aa.append(cnt)

    cnt = 1
    for i in range(1, m):
        if b[i] != b[i - 1]:
            bb.append(cnt)
            cnt = 1
        else:
            cnt += 1
    bb.append(cnt)

    if len(aa) != len(bb):
        print("NO")
        return

    for i in range(len(aa)):
        if aa[i] > bb[i] or aa[i] * 2 < bb[i]:
            print("NO")
            return

    print("YES")


t = int(input())
for _ in range(t):
    solve()

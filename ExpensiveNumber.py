t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    pos = False
    cnt0 = 0

    for i in range(n - 1, -1, -1):
        if s[i] != '0':
            pos = True
        elif pos:
            cnt0 += 1

    print(n - (cnt0 + 1))
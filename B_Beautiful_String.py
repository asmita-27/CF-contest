 
 
for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    pos = []
    for i in range(n):
        if s[i] == '0':
            pos.append(i + 1)

    print(len(pos))
    if pos:
        print(*pos)
    else:
        print()
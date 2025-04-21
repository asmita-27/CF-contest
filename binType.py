
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    trans = cnt01 = cnt10 = 0
    for i in range(n - 1):
        if s[i] != s[i+1]:
            trans += 1
            if s[i] == '0':
                cnt01 += 1
            else:
                cnt10 += 1

    init = 1 if s[0] == '1' else 0 
    if cnt01 >= 2 or cnt10 >= 2 or (init == 1 and cnt01 >= 1):
        gain = 2
    else: 
        if ((s[0] == '1' and s[-1] == '0')
            or (s[-1] == '0' and cnt01 >= 1)
            or (s[-1] == '1' and cnt10 >= 1)):
            gain = 1
        else:
            gain = 0 
    cost = n + trans + init - gain
    print(cost)


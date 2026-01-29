import math

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    res = s.count('1') 
    if res == 0:
        print((n + 2) // 3)
        continue
    i = 0
    while i < n:
        if s[i] == '0':
            j = i
            while j < n and s[j] == '0':
                j += 1
            leng = j - i
            l = (i > 0 and s[i - 1] == '1')
            r = (j < n and s[j] == '1')

            if l and r:
                if leng >= 2:
                    res += (leng - 2 + 2) // 3   
            else:
                res += (leng - 1 + 2) // 3
            i = j
        else:
            i += 1

    print(res)

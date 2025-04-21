
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = input().strip()

    d = s.count('-')
    u = s.count('_')

    if d < 2 or u < 1:
        print(0)
        continue
    x = d // 2
    z = d - x
    result = x * u * z
    print(result)

def maxNo(n, x, skills):
    skills.sort(reverse=True)
    t = 0
    members = 0
    for s in skills:
        members += 1
        if members * s >= x:
            t += 1
            members = 0

    return t

for _ in range(int(input())):
    n, x = map(int, input() .split())
    skills = list(map(int, input() .split()))
    res  = maxNo(n, x, skills)
    print(res)

t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    if c>=d:
        print("Gellyfish")
    else:
        print("Flower")
t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    if min(b,d)<=min(a,c):
        print("Gellyfish")
    else:
        print("Flower")

for i in range(int(input())):
    n=int(input())
    a,c=[n,n,n],0
    while a!=[0,0,0]:
        a=sorted(a)
        a[-1]=a[-2]//2
        c+=1
    print(c)

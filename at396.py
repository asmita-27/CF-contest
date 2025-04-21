def main():
    n = int(input())
    a = list(map(int,input().split()))
    count  =0
    for i in range(n-2):
        if a[i] == a[i+1] == a[i+2]:
            print("YES")
            return 
    print("NO")
main()
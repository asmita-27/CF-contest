def solve():
    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split())) 
        a.sort(reverse=True) 
        print(sum(a[:k+1]))

if __name__ == '__main__':
    solve()

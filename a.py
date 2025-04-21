def solve():
    t = int(input().strip())
    for _ in range(t):
        x, y = map(int, input().split()) 
        if x == y:
            print("NO")
        else:
            d = x - y + 1 
            if d >= 0 and d % 9 == 0:
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    solve()

t = int(input())
for _ in range(t):
    n = int(input())
    grid = [[0]*n for _ in range(n)]
    val = 0
    for d in range(2*n - 1):
        for i in range(n):
            j = d - i
            if 0 <= j < n:
                if d % 2 == 0:
                    grid[i][j] = val
                else:
                    grid[j][i] = val
                val += 1
    for row in grid:
        print(' '.join(map(str, row)))

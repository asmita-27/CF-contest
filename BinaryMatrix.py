for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = [input().strip() for _ in range(n)]
    results = []
    rowPar = [0] * n
    colPar = [0] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                rowPar[i] ^= 1
                colPar[j] ^= 1

    odd_rows = sum(rowPar)
    odd_cols = sum(colPar)

    results.append(max(odd_rows, odd_cols))
    print(*results) 


  
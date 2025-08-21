import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    
    if k == 0:
        S.sort()
        T.sort()
        print("YES" if S == T else "NO")
        continue
     
    count_S = [0] * k
    count_T = [0] * k

    for x in S:
        count_S[x % k] += 1
    for x in T:
        count_T[x % k] += 1
     
    ok = True
    for r in range((k + 1) // 2):  
        opp = (k - r) % k
        if r == opp:  
            if count_S[r] != count_T[r]:
                ok = False
                break
        else:   
            if count_S[r] + count_S[opp] != count_T[r] + count_T[opp]:
                ok = False
                break
    
    print("YES" if ok else "NO")

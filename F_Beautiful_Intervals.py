import sys

def solve_case(n, intervals):
    L_all = 1
    R_all = n
    for l, r in intervals:
        if l > L_all: L_all = l
        if r < R_all: R_all = r
    if L_all <= R_all:
        pos0 = L_all - 1 
        p = [-1] * n
        p[pos0] = 0
        cur = 1
        for i in range(n):
            if p[i] == -1:
                p[i] = cur
                cur += 1
        return p
    cover_intervals = [[] for _ in range(n)]  
    Lmax = [-10**9] * n
    Rmin = [10**9] * n
    for i in range(n):
        Lmax[i] = 1
        Rmin[i] = n
    for l, r in intervals:
        for i in range(l-1, r):
            if Lmax[i] < l:
                Lmax[i] = l
            if Rmin[i] > r:
                Rmin[i] = r

    chosen_i = -1
    chosen_j = -1
    for i in range(n):
        interL = Lmax[i]
        interR = Rmin[i]
        if interL <= interR:
            length = interR - interL + 1
            if length >= 2:
                if interL <= i+1 <= interR:
                    if interL < i+1:
                        jpos = interL - 1
                    else:
                        jpos = interR - 1
                else:
                    jpos = interL - 1
                chosen_i = i
                chosen_j = jpos
                break

    if chosen_i != -1:
        p = [-1] * n
        p[chosen_i] = 0
        p[chosen_j] = 1
        cur = 2
        for k in range(n):
            if p[k] == -1:
                p[k] = cur
                cur += 1
        return p
    cover_count = [0]*n
    for l,r in intervals:
        for i in range(l-1, r):
            cover_count[i] += 1
    pos0 = max(range(n), key=lambda x: cover_count[x])
    p = [-1]*n
    p[pos0] = 0
    cur = 1
    for i in range(n):
        if p[i] == -1:
            p[i] = cur
            cur += 1
    return p

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it)); m = int(next(it))
        intervals = []
        for _i in range(m):
            l = int(next(it)); r = int(next(it))
            intervals.append((l, r))
        p = solve_case(n, intervals)
        out_lines.append(" ".join(map(str, p)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()

import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        l, r = 0, n - 1
        ans = []
        last_vals = [] 
        
        def safe_with(val):
           
            tmp = last_vals + [val]
            run = 1
            dir = 0
            for i in range(len(tmp)-1, 0, -1):
                d = 1 if tmp[i] > tmp[i-1] else -1
                if dir == 0 or d == dir:
                    run += 1
                    dir = d
                else:
                    break
                if run >= 5:
                    return False
            return True
        
        while l <= r:
            cl = p[l]
            cr = p[r]
            okL = safe_with(cl)
            okR = safe_with(cr)
            if okL and not okR:
                pick, val = 'L', cl; l += 1
            elif okR and not okL:
                pick, val = 'R', cr; r -= 1
            else:
                if cl <= cr:
                    pick, val = 'L', cl; l += 1
                else:
                    pick, val = 'R', cr; r -= 1
            
            ans.append(pick)
            last_vals.append(val)
            if len(last_vals) > 4:
                last_vals.pop(0)
        
        print(''.join(ans))

if __name__ == "__main__":
    solve()

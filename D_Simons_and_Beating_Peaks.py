for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    left = [-1]*n
    right = [-1]*n
    parent = [-1]*n
    st = []
    
    for i in range(n):
        last = -1
        while st and a[st[-1]] < a[i]:
            last = st.pop()
        if st:
            right[st[-1]] = i
            parent[i] = st[-1]
        if last != -1:
            left[i] = last
            parent[last] = i
        st.append(i)
    
    root = parent.index(-1) 
    stk = [root]
    ans = 0
    
    while stk:
        mx = stk.pop()
        
        lft = 0 if left[mx] == -1 else 1
        rgt = 0 if right[mx] == -1 else 1
         
        def size(v):
            if v == -1: return 0
            s = 1
            if left[v] != -1: s += size(left[v])
            if right[v] != -1: s += size(right[v])
            return s
        
        lft = size(left[mx])
        rgt = size(right[mx])
        
        ans += min(lft, rgt) 
        if lft > rgt and left[mx] != -1:
            stk.append(left[mx])
        elif right[mx] != -1:
            stk.append(right[mx])
    
    print(ans)
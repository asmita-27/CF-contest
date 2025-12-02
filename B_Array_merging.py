from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    bestA = {}
    bestB = {}

    def fill(arr,mp):
        curr =1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                curr+=1
            else:
                mp[arr[i-1]]=max(mp.get(arr[i-1],0),curr)
                curr=1
        mp[arr[-1]]=max(mp.get(arr[-1],0),curr)
    fill(a,bestA)
    fill(b,bestB)
    ans = 1
    for key in bestA | bestB:
        ans = max(ans,bestA.get(key,0)+bestB.get(key,0))  
    print(ans)
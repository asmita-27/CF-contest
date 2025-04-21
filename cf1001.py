from collections import Counter

class Solution:
    def maxLength(self, arr):
        # code here
        
        freq = Counter(arr)
        maxLen =0
        for length , count in freq.items():
            if count>=2:
                maxLen = max(maxLen, 2*length)
            for otherLen, otherCount in freq.items():
                if length != otherLen and count>0 and otherCount >0:
                    comb = length + otherLen
                    if freq[length]>=1 and freq[otherLen]>=1:
                        maxLen = max(maxLen, comb)
        return maxLen
        

arr = list(map(int, input().split()))
print(maxLe(arr))
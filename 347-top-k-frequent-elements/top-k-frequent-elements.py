from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        
        a = Counter(nums)

        
        ta = sorted(a.items(), key=lambda item: item[1], reverse=True)

        
        for i in range(k):
            
            ans.append(ta[i][0])
            
        return ans


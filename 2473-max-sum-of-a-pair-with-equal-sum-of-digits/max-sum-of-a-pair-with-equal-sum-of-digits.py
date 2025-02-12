import numpy as np
class Solution:
    import numpy as np
    def maximumSum(self, nums: List[int]) -> int:
        ans=0
        d={}
        for i in  nums:
            
            
            k=i
            j = 0
            while k> 0:
                j+= k % 10  # Get last digit and add to total
                k //= 10
            if j in d :
                ans=max(ans,i+d[j])
            else:
                d[j]=i

            d[j]=max(d[j],i)
        if ans==0:
            return -1
        return ans
            
                   



        
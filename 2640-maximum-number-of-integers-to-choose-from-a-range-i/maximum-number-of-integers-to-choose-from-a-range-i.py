class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        start=1
        sum=0
        sa=set(banned)
        c=0
        while True:
            
            if start in sa:
                
                pass
                
             
            else:
                sum=sum+start
                if sum >maxSum:
                    sum=sum-start
                    c=c-1 
                c=c+1
                    
            start+=1
            if start >n:
                break
        return c 

       


            
        
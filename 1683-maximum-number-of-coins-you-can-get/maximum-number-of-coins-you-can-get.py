class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l=len(piles)//3
        ans=0
        j=0
       
        for i in piles[l:]:
            if j==0:
                ans+=i
                j=1
            else:
                j=0
        return ans 
            
            


        
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)
        piles.sort()
        l=n//3
        ans=0
        j=0
       
        for i in range(l,n,2):
            ans+=piles[i]
        return ans

            


        
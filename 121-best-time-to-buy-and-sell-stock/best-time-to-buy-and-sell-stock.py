class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pf=0
        val=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>val:
                pf = max(pf,prices[i]-val)
            elif prices[i]<val:
                val= min(val,prices[i])
            else:
                continue 

            
            
        return pf
            
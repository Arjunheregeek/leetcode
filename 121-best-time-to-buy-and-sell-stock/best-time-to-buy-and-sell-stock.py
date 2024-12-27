class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pf=0
        val=prices[0]
        for i in range(1,len(prices)):
            pf = max(pf,prices[i]-val)
            val= min(val,prices[i])
        return pf
            
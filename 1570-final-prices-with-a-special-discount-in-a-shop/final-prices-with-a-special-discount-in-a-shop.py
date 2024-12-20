class Solution(object):
    def finalPrices(self, prices):
        i =0
        j=1
        while True :
            if i==len(prices)-1:
                return prices
            
            if j>len(prices)-1:
                i+=1
                j=i+1
                

            if i==len(prices)-1:
                return prices
            if prices[j]<=prices[i]:
                prices[i]=prices[i]-prices[j]
                i+=1
                j=i+1
            elif  prices[j]>prices[i]:
                j+=1



        
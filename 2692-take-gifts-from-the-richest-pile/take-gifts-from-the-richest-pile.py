class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        l=0
        gifts.sort()
        n=len(gifts)-1

        while l<k:
            gifts[n]=int(sqrt(gifts[n]))
            gifts.sort()
            l+=1
        sum=0
        for i in range(n+1):
            sum=sum+gifts[i]
        return sum

        





        
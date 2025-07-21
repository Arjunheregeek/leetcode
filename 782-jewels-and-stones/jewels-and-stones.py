class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic={}
        ans=0
        for i in jewels:
            dic[i]=0

        for i in stones :
            if i in dic :
                ans+=1
        return ans 


        
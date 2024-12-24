class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        s=boxes
        ans=[0]*len(s)
        for i in range(len(s)):
            sum=0

            for j in range (len(s)):
                if int(s[j])>0 and j !=i:

                    k=abs(i-j)
                    sum= sum+k
                    
          
            ans[i]=sum
        return ans


        
class Solution:
    def sum_digit(self,x):
        ds = 0 
        while x>0 :
            ds += x%10 
            x //= 10

        return ds


    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        maxi = -1
        for i in nums :
            x = self.sum_digit(i)

            if x in dic :
                maxi=max(maxi,i+dic[x])
            else :
                dic[x]=i
            dic[x]=max(dic[x],i)

                
        return maxi

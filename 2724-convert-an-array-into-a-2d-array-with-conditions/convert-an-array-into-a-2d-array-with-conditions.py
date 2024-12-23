class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d=Counter(nums)
        ans=[]
        temp=[]
       
        while d:
            temp=[]

            for key , value in list( d.items()):
                if  d[key]>0:
                    temp.append(key)
                    d[key]-=1
                    if d[key]==0:
                        del d[key]
            ans.append(temp)
            
            
        return ans
                
            


        
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans=0
        j=min(nums)
        k=set(nums)

        for i in k:

            if i >0:
                ans+=i
            elif i>j:
                j=i
        if ans==0:
            return j
        else:
            return ans


        
            
            
            

            
            

        

        
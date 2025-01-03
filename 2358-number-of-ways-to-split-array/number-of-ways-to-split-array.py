class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        k=sum(nums)
        count=0
        summ=0
        for i in range (0,len(nums)-1):
            summ+=nums[i]
            
            if summ>=k-summ :
                count+=1
        return count 



        
            



        
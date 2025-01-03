class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        '''n=len(nums)
        left=[0]*n
        left[0]=nums[0]
        right=[0]*n
        right[n-1]=nums[n-1]
        for i in  range (1,n):
            left[i]=nums[i]+left[i-1]
        for i in range(n-2,-1,-1):
            right[i]=nums[i]+right[i+1]
        return right

        for i in range(0,n-1)'''
        k=sum(nums)
        count=0
        summ=0
        for i in range (0,len(nums)-1):
            summ+=nums[i]
            
            if summ>=k-summ :
                count+=1
        return count 



        
            



        
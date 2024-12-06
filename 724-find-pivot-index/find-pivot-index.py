class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            sum=sum+i
        leftsum=0
        for i in range(len(nums)):
            if i ==0 and sum-nums[i]==0:
                return 0 
            elif i ==len(nums)-1 and leftsum==0:
                return len(nums)-1
            else:
                sum=sum-nums[i]
                if leftsum==sum:
                    return i 
                leftsum=leftsum+nums[i]
        return -1
                
                

            
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        su=0
        max_sum=0
        if len(nums)==1:
            return nums[0]
       
        for i in range(len(nums)):
            
            su+=nums[i]
            if su<0:
                su=0
            max_sum=max(su,max_sum)
        if max_sum==0:
            return max(nums)
        return max_sum



        
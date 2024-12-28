class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        su=0
        max_sum=0
        if len(nums)==1:
            return nums[0]
        val=-9999999
        for i in range(len(nums)):
            val=max(val,nums[i])
            su+=nums[i]
            if su<0:
                su=0
            max_sum=max(su,max_sum)
        if max_sum==0:
            return val
        return max_sum



        
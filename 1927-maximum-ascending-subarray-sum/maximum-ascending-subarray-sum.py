class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summ=nums[0]
        tsum=summ

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                tsum+=nums[i]
                summ=max(tsum,summ)
            else:
                tsum=nums[i]
        return summ



        
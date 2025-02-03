class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans=1
        tempi=1
        tempd=1
        for i in range (1,len(nums)):
            if nums[i]>nums[i-1]:
                tempi+=1
                tempd=1
            elif nums[i]<nums[i-1]:
                tempd+=1
                tempi=1
            else:
                tempd=1
                tempi=1
            ans=max(ans,tempi,tempd)
        return ans 
            
        
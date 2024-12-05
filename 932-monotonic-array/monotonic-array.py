class Solution:
    def isMonotonic(self, nums: List[int]) -> list:
        if len(nums) in [0,1]:
            return True
        j=0
        for i in range(1,len(nums)):
            if j==0:
                if nums[i]<nums[i-1]:
                    j=1
                elif nums[i]>nums[i-1]:
                    j=2
                else:
                    j=0
            if j==1:


                if nums[i]<=nums[i-1]:

                    continue
                else:
                    return False
            if j==2:
                if nums[i]>=nums[i-1]:
                    continue
                else:
                    return False
        return True


            
                

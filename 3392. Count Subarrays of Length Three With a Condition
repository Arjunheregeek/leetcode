class Solution(object):
    def countSubarrays(self, nums):
        start=0
        end=2
        count=0
        while end<len(nums) :
            if (nums[start]+nums[end])*2==int(nums[start+1]):
                count+=1
                
            start+=1
            end+=1
        return count
            
            
        
        

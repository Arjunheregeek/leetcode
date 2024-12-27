class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sam=[0]*len(nums)
        for i in nums:
            if sam[i]!=0:
                return i 
            sam[i]=1


       

        
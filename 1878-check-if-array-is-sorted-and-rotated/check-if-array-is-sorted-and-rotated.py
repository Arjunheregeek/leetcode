class Solution:
    def check(self, nums: List[int]) -> bool:
        n=0
        i=1
        while i <len(nums):

            if nums[i]<nums[i-1]:
                n+=1
            i+=1
        if nums[-1]>nums[0]:
            n += 1
        if n<=1:
            return True
        else:
            return False



        
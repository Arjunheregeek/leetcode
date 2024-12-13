class Solution(object):
    def rotate(self, nums, k):
        ans=[0]*len(nums)
        for i in range (len(nums)):
            ans[(i+k)%len(nums)]=nums[i]
        for i in range (len(nums)):
            nums[i]=ans[i]
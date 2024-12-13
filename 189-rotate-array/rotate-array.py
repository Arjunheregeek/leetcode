class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        ans=[0]*n
        for i in range (n):
            ans[(i+k)%n]=nums[i]
        for i in range (n):
            nums[i]=ans[i]
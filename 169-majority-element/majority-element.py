class Solution(object):
    def majorityElement(self, nums):
        count=Counter(nums)
        return max(count,key=count.get)


        
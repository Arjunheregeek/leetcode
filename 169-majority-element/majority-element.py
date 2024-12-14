class Solution(object):
    def majorityElement(self, nums):
        count=Counter(nums)
        for i, value in count.items():
            if value> len(nums)/2:
                return i 


        
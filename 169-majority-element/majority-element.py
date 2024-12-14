class Solution(object):
    def majorityElement(self, nums):
        count=Counter(nums)
        keyvalue= [key for key,value in count.items() if value>len(nums)/2]
        return keyvalue[0]
        
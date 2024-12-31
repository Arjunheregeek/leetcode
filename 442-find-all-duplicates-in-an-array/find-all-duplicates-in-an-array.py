from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''snd = []
        for i in range(len(nums)):
            
            index = abs(nums[i]) - 1
           
            if nums[index] < 0:
                snd.append(index + 1)
            else:
               
                nums[index] = -nums[index]
        return snd'''
        a=set()
        ans=[]
        for i in nums:
            if i in a:
                ans.append(i)
            else:
                a.add(i)
        return ans
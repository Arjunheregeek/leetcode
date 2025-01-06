class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=[]
        for key,value in count.items():
            if count[key]<2:
                ans.append(key)
        return ans 
            
        
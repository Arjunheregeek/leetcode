class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=len(nums)//2
        po=[]
        ne=[]
        ans=[]
        for i in nums:
            if i >=0:
                po.append(i)
            else:
                ne.append(i)
        for i in range (a):
            ans.append(po[i])
            ans.append(ne[i])
        return ans




        
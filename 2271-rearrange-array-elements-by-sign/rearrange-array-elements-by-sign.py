class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        '''a=len(nums)//2
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
        return ans'''
        
        ans=[0]*len(nums)
        p=0
        n=1
        for i in range(len(nums)):
            if nums[i]>=0:
                ans[p]=nums[i]
                p+=2
            else:
                ans[n]=nums[i]
                n+=2
        return ans

            




        
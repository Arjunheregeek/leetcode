class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       

        
        n=len(nums)
        answer=[1]*n
        left=[1]*n
        right=[1]*n
        for i in range(n):
            if i ==0:
                left[0]=1
            else:
                left[i]=left[i-1]*nums[i-1]
        for i in range(n-1,-1,-1):
            if i == n-1:
                right[i]=1
            else:
                right[i]= right[i+1]*nums[i+1]
        for i in range(n):
            answer[i]=left[i]*right[i]
        return answer
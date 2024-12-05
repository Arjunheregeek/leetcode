class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        t=0
        left=0
        right=len(height)-1

        while left<=right and right>0 and left<len(height)-1:
            res=(right-left)*min(height[left],height[right])
            if res>t:
                t=res
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1
            
        return t

        
            





        
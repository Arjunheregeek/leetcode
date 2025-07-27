class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        i = 1
        n = len(nums)
        while i < len(nums)-1 :
            if nums[i] > nums[i-1]  :
                while i < len(nums)-1 and nums[i] == nums[i+1] :
                    i+=1 
                    
                if i < n-1 and nums[i] > nums[i+1]  :  
                    ans +=1 
                i+=1
                continue 
                
            elif nums[i] < nums[i-1] :
                while  i < n-1 and nums[i+1] == nums[i]:
                    i+= 1
                if i < n-1 and nums[i]< nums[i+1]:
                    ans +=1
                
                i += 1
                continue 
            i+=1
        return ans
                
        
                
            
            
            
        
        
        
        
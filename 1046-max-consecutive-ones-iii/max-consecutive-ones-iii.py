class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        c = k  
        ma = 0
        if len(nums)==0:
            return 0

        for end in range(len(nums)):
            if nums[end] == 0:
                c -= 1  

            
            while c < 0:
                if nums[start] == 0:
                    c += 1  
                start += 1  

            
            ma = max(ma, end - start + 1)

        return ma

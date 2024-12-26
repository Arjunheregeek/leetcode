

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        k = 0
        count = 0
        
        while k < len(arr):
          
            max_so_far = max(arr[:k + 1])
            
           
            if max_so_far == k:
                count += 1
            
            k += 1  #
        
        return count

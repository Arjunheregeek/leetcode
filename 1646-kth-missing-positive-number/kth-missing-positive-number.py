class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
       
        start=0
        count=0

        while True:
            if start not in arr :
                if count==k:
                    return start
               
                count+=1
            start+=1
            
            

        
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        index =0
        start=0
        count=0

        while True:
            if start not in arr :
                if count==k:
                    return start
                start+=1
                count+=1
            else:
                start+=1
            

        
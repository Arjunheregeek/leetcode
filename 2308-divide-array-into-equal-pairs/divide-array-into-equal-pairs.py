class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        dic = Counter(nums) 
        for val in dic.values():
            if val%2 != 0:
                return False 

        return True
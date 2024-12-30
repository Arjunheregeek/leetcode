class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        a=set()
        for i in nums:
            a.add(i)
            x = str(i)[::-1]
            a.add(int(x))
        return len(a)



        
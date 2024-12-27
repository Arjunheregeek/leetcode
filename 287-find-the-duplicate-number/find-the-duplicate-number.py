class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cou=Counter(nums)
        return max(cou, key=cou.get)

        
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        for num in nums:
            if num == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return len(nums) - l
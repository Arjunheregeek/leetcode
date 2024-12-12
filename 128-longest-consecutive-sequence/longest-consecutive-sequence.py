class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        c = 1
        final = 0
        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1] + 1:

                c = c + 1
                final = max(final, c)
            elif  nums[i] == nums[i - 1]  :
                continue

            else:

                c = 1
        return max(final, c)

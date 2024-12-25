class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        c = k  # Remaining flips
        ma = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                c -= 1  # Use a flip

            # If flips are exhausted, shrink the window
            while c < 0:
                if nums[start] == 0:
                    c += 1  # Restore a flip
                start += 1  # Move the start pointer

            # Update the maximum length of the window
            ma = max(ma, end - start + 1)

        return ma

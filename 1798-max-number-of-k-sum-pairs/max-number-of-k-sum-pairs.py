class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter

        # Count frequencies of all numbers
        counts = Counter(nums)
        c = 0

        for num in counts:
            complement = k - num
            if complement in counts:
                if complement == num:
                    # Special case: if num and complement are the same
                    c += counts[num] // 2
                else:
                    # Count pairs from num and complement
                    c += min(counts[num], counts[complement])

                # Ensure we don't reuse these numbers
                counts[complement] = 0
                counts[num] = 0

        return c

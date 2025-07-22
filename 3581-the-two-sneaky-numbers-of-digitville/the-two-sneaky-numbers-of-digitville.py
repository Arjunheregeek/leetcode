from collections import Counter
from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Create a Counter object from the list
        k = Counter(nums)
        ans = []
        # Iterate over the items (key-value pairs) of the Counter
        for key, value in k.items():
            if value > 1:
                ans.append(key)
        return ans
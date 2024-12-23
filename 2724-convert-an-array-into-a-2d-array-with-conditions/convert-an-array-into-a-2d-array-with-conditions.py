from collections import Counter
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Count the frequency of each number
        count = Counter(nums)
        
        # Step 2: Create the result list
        result = []

        # Step 3: Create a list of buckets based on the frequency of each number
        max_frequency = max(count.values())  # The number of rows needed is determined by the max frequency
        buckets = [[] for _ in range(max_frequency)]

        # Step 4: Distribute the numbers into the buckets
        for num, freq in count.items():
            for i in range(freq):
                buckets[i].append(num)
        
        # Step 5: Return the result by collecting the rows from the buckets
        result = buckets
        return result

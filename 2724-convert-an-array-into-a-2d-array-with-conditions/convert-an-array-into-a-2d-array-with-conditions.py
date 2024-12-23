from collections import defaultdict

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        element_map = defaultdict(list)
        for idx, num in enumerate(nums):
            element_map[num].append(idx)
        
        max_rows = max(len(indices) for indices in element_map.values())
        result = [[] for _ in range(max_rows)]
        for num, indices in element_map.items():
            for i in range(len(indices)):
                result[i].append(num)
        
        return result
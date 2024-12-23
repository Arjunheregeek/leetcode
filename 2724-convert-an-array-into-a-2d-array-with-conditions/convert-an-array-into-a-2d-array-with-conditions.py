class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Count the frequency of each number
        count = Counter(nums)
        
        # Initialize the result list
        result = []
        
        # The number of rows will be the maximum frequency
        max_frequency = max(count.values())
        
        # Create the result array by filling rows one at a time
        for i in range(max_frequency):
            row = []
            for key, freq in count.items():
                if freq > 0:
                    row.append(key)
                    count[key] -= 1  # Decrease the frequency of the number
            result.append(row)
        
        return result

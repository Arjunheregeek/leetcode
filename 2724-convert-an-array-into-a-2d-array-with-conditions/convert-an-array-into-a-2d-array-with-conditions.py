class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Create a Counter to count occurrences of each number
        count = Counter(nums)
        
        # Initialize the result list
        ans = []
        
        # While there are still elements to distribute
        while count:
            row = []
            # Collect numbers that can be added to this row
            for key in list(count):
                if count[key] > 0:
                    row.append(key)
                    count[key] -= 1
                    if count[key] == 0:
                        del count[key]  # Remove the key once its count reaches 0
            
            # Add the formed row to the answer
            ans.append(row)
        
        return ans
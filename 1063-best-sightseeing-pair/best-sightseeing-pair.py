class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0  # Initialize maximum score
        max_value = values[0]  # Start with the first value adjusted for i (values[i] + i)
        
        for j in range(1, len(values)):
            # Calculate the score for the pair (i, j)
            max_score = max(max_score, max_value + values[j] - j)
            
            # Update max_value to consider the best i so far
            max_value = max(max_value, values[j] + j)
        
        return max_score

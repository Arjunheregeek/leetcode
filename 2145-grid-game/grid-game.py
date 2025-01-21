class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Calculate suffix sums for both rows
        row1 = [0] * n  # Top row suffix sum
        row2 = [0] * n  # Bottom row suffix sum

        row1[n-1] = grid[0][n-1]
        row2[n-1] = grid[1][n-1]

        for i in range(n-2, -1, -1):
            row1[i] = grid[0][i] + row1[i+1]
            row2[i] = grid[1][i] + row2[i+1]

        # Minimize the second robot's maximum score
        min_second_robot_score = float('inf')
        bottom_sum = 0  # Prefix sum for the bottom row

        for i in range(n):
            # Calculate remaining sums for both rows
            top_remaining = row1[i+1] if i+1 < n else 0
            bottom_remaining = bottom_sum

            # Calculate the second robot's score for this split
            second_robot_score = max(top_remaining, bottom_remaining)
            min_second_robot_score = min(min_second_robot_score, second_robot_score)

            # Update bottom prefix sum for the next column
            bottom_sum += grid[1][i]

        return min_second_robot_score

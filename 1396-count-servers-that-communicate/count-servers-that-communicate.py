class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        summ = 0  # Total count of servers
        c = 0  # Row counter
        lone = []  # List to store indices of rows with exactly one server
        
        # First pass: Calculate total servers and track rows with one server
        for row in grid:
            k = sum(row)  # Count servers in the current row
            if k == 1:  # Append the row index if it has one server
                lone.append(c)
            summ += k
            c += 1
        
        lon = 0  # Count of lone servers that are not connected
        
        # Check lone servers in their respective columns
        while len(lone) != 0:
            row_index = lone.pop()  # Get the row index
            col_index = -1
            # Find the column index of the server in the current row
            for i in range(len(grid[0])):
                if grid[row_index][i] == 1:
                    col_index = i
                    break
            
            # Check if the server in this column has any other servers
            connected = False
            for r in range(len(grid)):
                if r != row_index and grid[r][col_index] == 1:
                    connected = True
                    break
            
            # If no connection is found, increment lone count
            if not connected:
                lon += 1
        
        return summ - lon  # Subtract lone servers from the total

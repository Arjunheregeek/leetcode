class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for k in range(n):
            arr = []
            i, j = k, 0

            while i < n:
                arr.append(grid[i][j])
                i += 1
                j += 1
            
            arr.sort(reverse=True)
            i, j = k, 0

            while i < n:
                grid[i][j] = arr[j]
                i += 1
                j += 1
        
        for k in range(1, n):
            arr = []
            i, j = 0, k

            while j < n:
                arr.append(grid[i][j])
                i += 1
                j += 1
            
            arr.sort()
            i, j = 0, k

            while j < n:
                grid[i][j] = arr[i]
                i += 1
                j += 1
        
        return grid
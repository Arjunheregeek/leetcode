class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row1=[]
        col1=[]
        n=len(grid)
        m=len(grid[0])
        for row in grid:
            c=Counter(row)
            if 1 in c:
                row1.append(c[1])
            else:
                row1.append(0)
        for col in zip(*grid):
            k=Counter(col)
            if 1 in k:

                col1.append(k[1])
            else:
                col1.append(0)
        for i in range(n):
            for j in range(m):
                grid[i][j]=row1[i]+col1[j]-(n-row1[i])-(m-col1[j])
        return grid

                



        
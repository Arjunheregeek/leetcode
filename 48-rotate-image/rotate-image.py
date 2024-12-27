class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        a = len(matrix)
        rotated = copy.deepcopy(matrix)
        for  i in range (a):


            for j in range (a):
                matrix[j][a-1-i]=rotated[i][j]
        
        
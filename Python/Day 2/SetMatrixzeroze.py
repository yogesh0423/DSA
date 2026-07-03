class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        col0 = 1

        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0
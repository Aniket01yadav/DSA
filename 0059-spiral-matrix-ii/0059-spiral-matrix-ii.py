class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        row_start, row_end = 0, n - 1
        col_start, col_end = 0, n - 1
        num = 1
        total = n * n
        
        while num <= total:
            
            for j in range(col_start, col_end + 1):
                matrix[row_start][j] = num
                num += 1
                
            row_start += 1
            
            for i in range(row_start, row_end + 1):
                matrix[i][col_end] = num
                num += 1
            col_end -= 1
            
            for j in range(col_end, col_start - 1, -1):
                matrix[row_end][j] = num
                num += 1
            row_end -= 1
            
            for i in range(row_end, row_start - 1, -1):
                matrix[i][col_start] = num
                num += 1
            col_start += 1
            
        return matrix
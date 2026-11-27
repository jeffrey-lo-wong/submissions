class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
    #     zeros = []

    #     for row in range(len(matrix)):
    #         for col in range(len(matrix[row])):
    #             if matrix[row][col] == 0:
    #                 zeros.append((row, col))

    #     for row, col in zeros:
    #         self.helper(matrix, row, col)

    # def helper(self, matrix, row, col):
    #     for r in range(len(matrix)):
    #         matrix[r][col] = 0
    #     for c in range(len(matrix[0])):
    #         matrix[row][c] = 0
        
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

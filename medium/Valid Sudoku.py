class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # For rows and columns, create arrays to keep track of numbers in each given row 1-9 and column 1-9
        rows = [[], [], [], [], [], [], [], [], []]
        columns = [[], [], [], [], [], [], [], [], []]
        # For 3x3 sub-boxes, we must use a dictionary holding a set because our keys will be tuples
        sub_boxes = defaultdict(set)

        # Iterate through each cell, by row and column, in the 9x9 Sudoku board
        for row in range(9):
            for col in range(9):
                n = board[row][col] # Current cell's number

                if n == ".":
                    continue # Skip past "." cells

                if n in rows[row] or n in columns[col] or n in sub_boxes[(row // 3, col // 3)]:
                    return False # If n violates Sudoku rules our board is invalid
                
                rows[row].append(n)
                columns[col].append(n)
                sub_boxes[(row // 3, col // 3)].add(n)

        return True # No violations found, thus board is valid

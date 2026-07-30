class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        nums = "123456789"
        rows = {}
        for r in range(9):
            rows[r] = set()
        columns = {}
        for r in range(9):
            columns[r] = set()
        squares ={}
        for r in range(9):
            squares[r] = set()


        #for row in board:
        for row in range(9):  #iterate through each row
            #print(row)
            for col in range(9): #iterate through each col
                num = board[row][col]
                if num in nums:    #if a number
                    if (num in rows[row]) or (num in columns[col]): #check rows&cols
                        return False
                    else:
                        rows[row].add(num)
                        columns[col].add(num)
                    square = (row//3)*3 + (col//3)
                    if num in squares[square]:
                        return False
                    else: squares[square].add(num)

                    



        return True



        board=[
            [".",".","4",".",".",".","6","3","."],
            [".",".",".",".",".",".",".",".","."],
            ["5",".",".",".",".",".",".","9","."],
            [".",".",".","5","6",".",".",".","."],
            ["4",".","3",".",".",".",".",".","1"],
            [".",".",".","7",".",".",".",".","."],
            [".",".",".","5",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."]]

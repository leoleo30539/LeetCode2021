class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            board_t = zip(*board)
            if len([x for x in board[i] if x != '.']) != len(set(board[i]))-1:
                return False
            if len([x for x in board_t[i] if x != '.']) != len(set(board_t[i]))-1:
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = []
                for k in range(3):
                    temp += board[i+k][j:j+3]
                if len([x for x in temp if x != '.']) != len(set(temp))-1:
                    print(3)
                    return False
                    
        return True
        

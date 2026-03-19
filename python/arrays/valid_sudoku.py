class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #O(1)
        for i in range(9):
            for j in range(9):
                #we need to make 3 checks for each number
                #first check is in the horizontal
                if board[i][j] == "." : continue
                for index in range(9):
                    if not index == j: 
                        #horizontal check
                        if board[i][j] == board[i][index]: return False
                    if not index == i:
                        #vertical check
                        if board[i][j] == board[index][j]: return False
                #now we have to check the box
                #getting the start of the box
                start_i = (i//3) * 3
                start_j = (j//3) * 3
                for box_i in range(start_i, start_i + 3):
                    for box_j in range(start_j, start_j + 3):
                        if box_i == i and box_j == j: continue

                        if board[box_i][box_j] == board[i][j]: return False      
        return True
        
turncounter = 1
rows = 3
cols = 3
shouldQuit = False

board = [["0" for i in range(cols)] for j in range(rows)]


print(board)

movesdict = {
    "222100011": ["2 0 2 2 0 0 0 1 1", "2 0 2 1 2 0 0 1 1", "2 2 0 1 0 2 0 1 1"],
    "222010101": ["0 2 2 2 1 0 1 0 1", "0 2 2 0 2 0 1 0 1"],
    "202210001": ["0 0 2 2 2 0 0 0 1", "2 0 0 2 2 0 0 0 1", "2 0 2 0 1 0 2 0 1", "2 0 0 2 1 2 0 0 1"],



}

def initialize_board(board):
    board[0][0] = "2"
    board[0][1] = "2"
    board[0][2] = "2"

    board[1][0] = "0"
    board[1][1] = "0"
    board[1][2] = "0"

    board[2][0] = "1"
    board[2][1] = "1"
    board[2][2] = "1"

def board_to_string(board):
    result_string = ""
    for row in board:
        for element in row:
            result_string = result_string + str(element)

    return result_string


#while not shouldQuit:
#    a = 0

initialize_board(board)
print(board_to_string(board))
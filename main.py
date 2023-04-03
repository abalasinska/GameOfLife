from board import init, display
from config import Settings

settings = Settings()

width = settings.width
height = settings.height

board = init(width, height)

board[4][5] = 1
board[4][6] = 1
board[5][5] = 1

display(board)

'''for x in range(height):
    row = []
    for y in range(width):
        row.append(0)
    board.append(row)'''

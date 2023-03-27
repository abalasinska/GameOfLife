def display (board):
    for row in board:
        print(row)
    return

def init (WIDTH,HEIGHT):
    board = []
    for x in range(HEIGHT):
        row = []
        for y in range(WIDTH):
            row.append(0)
        board.append(row)
    return board
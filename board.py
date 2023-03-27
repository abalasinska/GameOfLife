def init (width: int, height: int) -> list:
    """
    Creates a 2D list of zeros with the given width and height.
    """
    board = []

    for x in range(height):
        row = []
        for y in range(width):
            row.append(0)
        board.append(row)
    return board


def display (board: list):
    for row in board:
        print(row)
    
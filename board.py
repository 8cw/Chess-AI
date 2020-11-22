BOARDSIZE = 8
board = []

FILE_LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h"]

ROW_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]

UNICODE_PIECE_SYMBOLS = {
    "R": "♖", "r": "♜",
    "N": "♘", "n": "♞",
    "B": "♗", "b": "♝",
    "Q": "♕", "q": "♛",
    "K": "♔", "k": "♚",
    "P": "♙", "p": "♟",
    "·": "·"
}

def create_board(board: list) -> list:
    """
    A function that creates the board object.\n

    Creates a 8x8 grid of list which contains the piece occupying the square.
    """

    #Creates board object
    board = [
        ["R", "N", "B", "K", "Q", "B", "N", "R"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["·", "·", "·", "·", "·", "·", "·", "·"],
        ["·", "·", "·", "·", "·", "·", "·", "·"],
        ["·", "·", "·", "·", "·", "·", "·", "·"],
        ["·", "·", "·", "·", "·", "·", "·", "·"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["r", "n", "b", "k", "q", "b", "n", "r"]
    ]

    return board

def printannotatedboard():
    """
    A function that prints the board showing the piece occupying the square with notation printed along the side of the board.\n

     - At the start of every row it prints the row number.
     - At the bottom of every column it prints the column letter.
     - Prints the piece in the square list.
      - If there is no piece, a · will be printed.
      - If there is a piece, the appropriate piece will be printed.
    """

    row_num = BOARDSIZE - 1
    for row in board:
        print(ROW_NUMBERS[row_num], end =" ")
        for square in row:
            print(f"{UNICODE_PIECE_SYMBOLS.get(square)} ", end =" ")
        print("")
        row_num -= 1

    #Prints the file letter
    print(" ", end =" ")
    for i in range(BOARDSIZE):            
        print(f"{FILE_LETTERS[i]} ", end =" ")

board = create_board(board)

printannotatedboard()
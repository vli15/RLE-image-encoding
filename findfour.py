#Vivian Li
#COP 3504C

#need to fix players switching when there is an error (fixed)
#need to fix filling up whole column when inserting a chip (fixed)
#need to define min and max rows/columns (done)
#need to figure out win method ISNT WORKING
def get_initial_board(rows: int, columns: int):
    board = list()
    c = list()
    for i in range(columns):
        c.append('.')
    for i in range(rows):
        board.append(c[:])
    return board

def print_board(board: list[list[str]]):
    print(' ', end='')
    top = '_'*(len(board[0])*2-1)
    print(top, end='')
    print('')
    rows = len(board)
    for i in range(rows-1, -1, -1):
        print('|', end='')
        for point in board[i]:
            print(point, end=' ')
        print('|')
    print(' ', end='')
    bottom = '-' * (len(board[0]) * 2 - 1)
    print(bottom)

def insert_chip(board: list[list[str]], column: int, chip: str):
    if column < 0 or column > len(board):
        print("Error: no such column!", end='')
        return
    rows = len(board) #max amount of rows and columns (since perfect square)
    if board[rows-1][column] != '.': #looking at the top most element
        print("Error: Column is full!", end='')
        return
    #start from the bottom and look up
    for i in range(rows):
        if board[i][column] == '.':
            board[i][column] = chip
            print("row: ", i)
            print("column: ", column)
            return i

def is_win_state(chip: str, board: list[list[str]], row: int, column: int):
    vertical = True
    horizontal = False
    '''vertical will start as true and if there is a discrepancy, it will turn false since there is only one way of checking'''
    for i in range(row, row-4, -1):
        if board[i][column] != chip:
            vertical = False
            break
    """starting from the end of the row and checking to see if there is four in a row"""
    j = 0
    counter = 0
    for element in board[row]:
        if element == chip:
            counter +=1
        else:
            counter = 0
            continue
        if counter == 4:
            horizontal = True
            break
    if horizontal or vertical: #hopefully evaluates as booleans and if one is true, then will return true
        return True
    else:
        return False

def is_board_full(board: list[list[str]]):
    for row in board:
        for point in row:
            if point == '.':
                return False
    return True

def main():
    winner = 0
    print("Welcome to Find Four!")
    print("---------------------")
    while(True):
        r = int(input("Enter height of board (rows): "))
        if r < 4:
            print("Error: height must be at least 4!")
        elif r > 25:
            print("Error: height can be at most 25!")
        else:
            break
    while (True):
        c = int(input("Enter width of board (columns): "))
        if c < 4:
            print("Error: width must be at least 4!")
        elif c > 25:
            print("Error: width can be at most 25!")
        else:
            break
    board = get_initial_board(r, c)
    print_board(board)
    print("\nPlayer 1: x")
    print("Player 2: o")
    player = 1
    chip = 'x'
    player2 = 2
    chip2 = 'o'
    #figure out loop mechanics
    while(is_board_full(board) != True):
        try:
            print("\nPlayer", player, " - Select a Column: ", end='')
            col = int(input())
            row = insert_chip(board, col, chip)
            if row == None: #got an error --> column is full
                continue
            else:
                print_board(board)
                if is_win_state(chip, board, row, col):
                    winner = player
                    break
                # switching players
                if player == 1:
                    player = 2
                    chip = 'o'
                elif player == 2:
                    player = 1
                    chip = 'x'
        except:
            print("Error: not a number!", end = '')
    if winner != 0:
        print("\nPlayer", winner, "won the game!")
    else:
        print("\nDraw game! Players tied.")
if __name__ == "__main__":
    main()
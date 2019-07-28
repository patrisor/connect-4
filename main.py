def print_board(b):
    inp = [[' ' for x in range(7)] for y in range(6)]
    for r in range(len(b)): #Convert board list to a new string Array
        for c in range(len(b[r])):
            if b[r][c] == 0:
                continue
            inp[r][c] = ('R' if b[r][c] == 1 else 'Y')
    print("\n  1   2   3   4   5   6   7")
    for i in range(len(inp)):
        print("| " + inp[i][0] + " | " + inp[i][1] + " | " + inp[i][2] + " | " + inp[i][3] + " | " + 
                inp[i][4] + " | " + inp[i][5] + " | " + inp[i][6] + " |")

def update_board(b, i, p): # Traverses grid from bottom-up to be as efficient as possible in checking grid
    if i >= 7 or i <= -1:
        return -1
    for r in range(len(b) - 1, -1, -1):
        if b[r][i] == 0:
            b[r][i] = (2 if p == "Player 2" else 1)
            return 1
    return 0

def determine_player(p):
    return("Player 1" if p == "Player 2" else "Player 2")

def check_ties(board):
    hit = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                hit += 1
    return (hit == 0)

# Thanks to 4castle on StackExchange forums for teaching the algorithm
# (https://codereview.stackexchange.com/questions/127091/java-connect-four-four-in-a-row-detection-algorithms)
def check_win(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                continue # don't check empty slots
            if (((c + 3) < len(board[r])) and (board[r][c] == board[r][c + 1]) and 
            (board[r][c] == board[r][c + 2]) and (board[r][c] == board[r][c + 3])):
                return board[r][c] # checks side to side
            if ((r + 3) < len(board)):
                if (((board[r][c] == board[r + 1][c]) and (board[r][c] == board[r + 2][c]) and 
                (board[r][c] == board[r + 3][c])) or (((c + 3) < len(board[r])) and 
                (board[r][c] == board[r + 1][c + 1]) and (board[r][c] == board[r + 2][c + 2]) and 
                (board[r][c] == board[r + 3][c + 3])) or (((c - 3) >= 0) and (board[r][c] == board[r + 1][c - 1]) 
                and (board[r][c] == board[r + 2][c - 2]) and (board[r][c] == board[r + 3][c - 3]))):
                    return board[r][c] # checks up and diagonally
    return 0 # no winner found

def game_engine(BOARD, player):
    while True:
        player = determine_player(player)
        print_board(BOARD)
        while True:
            inp = input(player + " Enter position:\n")
            if inp == "q":
                return(1)
            if not inp.isdigit():
                print("Not a digit, try again.")
                continue
            upd = update_board(BOARD, int(inp) - 1, player)
            if upd == 1:
                break
            else:
                print(("Column is full. Find different position." if upd == 0 else "Column Doesn't exit. Try Again!"))
        check = check_win(BOARD)
        if ((check == 1) or (check == 2)):
            print_board(BOARD)
            print(("Player 1" if check == 1 else "Player 2") + " has won the game!")
            break
        if check_ties(BOARD):
            print_board(BOARD)
            print("TIE. No space left on board!")
            break
    return(0)

if __name__ == "__main__":
    BOARD = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
    player = "Player 2"
    exit(game_engine(BOARD, player))

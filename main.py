# TODO: Update
def print_board(b):
  print(" 1  2  3  4  5  6  7")
  for r in range(len(b)):
    print(b[r])

def update_board(b, i, p):
  # Traverse array to manipulate it
  for r in range(len(b) - 1, -1, -1):
    if b[r][i] == 0:
      b[r][i] = (2 if p == "Player 2" else 1)
      return True
  return False

def determine_player(p):
  return("Player 1" if p == "Player 2" else "Player 2")

def main():
  BOARD = [[0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0]]
  player = "Player 2"
  while True:
    # Determine player
    player = determine_player(player)
    # Print board
    print_board(BOARD)
    # User input
    inp = int(input(player + " Enter position:\n")) - 1
    # TODO: Update board
    if update_board(BOARD, inp, player):
      print("SUCCESS")
    else:
      print("Column is Full")

if __name__=="__main__":
  main()

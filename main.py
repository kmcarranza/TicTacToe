# Tic Tac Toe Game

user = True 
counter = 0
conv_user_input = 0
conv_counter = 0

# This is Creating the Gameboard
game_board = ["-","-","-",
              "-","-","-",
              "-","-","-"] 

# This will display Gameboard
def display_board():
  print('  A   B   C')
  print("1 "+ game_board[0] +" | "+game_board[1] +" | "+ game_board[2])
  print("2 "+ game_board[3] +" | "+game_board[4] +" | "+ game_board[5])
  print("3 "+ game_board[6] +" | "+game_board[7] +" | "+ game_board[8])

# This will clear all moves on board for new game
def clear_board(game_board):
  for i in range(len(game_board)):
    game_board[i] = "-"
  return game_board

# Checks to make sure inputs are within range of board 
def check_boundary(user_input):
  if user_input >9 or user_input < 1:
    print("This is not a valid input.")
    print("Please enter a position A1 to A9 or enter \"q\" to quit:")
    return False
  else:return True

# Ability to end game before winner or tie is achieved. 
def quit(user_input):
  if user_input =="q": 
    print("Great Game. Thank you for playing.")
    return True
  else: return False

# Checks to see if selected option is already taken 
def istaken(user_input):
  if game_board[user_input] == "x" or game_board[user_input] =="o":
    return True
  else: return False

# Updates board to x or os 
def update_board(user_input,active_user):
  game_board[user_input] = active_user
  counter
  return counter 

# Switches users between x and o
def current_user(user):
  if user: return "x"
  else: return "o"

# Gameboard selections are A1-C3 and transformed to numeric values
def user_input_transform(user_input):
  conv_user_input = 10
  if user_input == 'A1':
    conv_user_input = 1
  if user_input == "A2":
    conv_user_input = 4
  if user_input == "A3":
    conv_user_input = 7
  if user_input == "B1":
    conv_user_input = 2
  if user_input == "B2":
    conv_user_input= 5
  if user_input == "B3":
    conv_user_input = 8
  if user_input == "C1":
    conv_user_input = 3
  if user_input == "C2":
    conv_user_input = 6
  if user_input == "C3":
    conv_user_input = 9
  return conv_user_input

# Checks to see if winner from Rows, Columns, or Diagonal
def did_win(game_board,active_user):
    if check_win_row(game_board,active_user): 
      return True
    if check_win_col(game_board,active_user): 
      return True
    if check_diagonal(game_board,active_user): 
      return True
    else:return False

# Checks to see if any winners via row
def check_win_row(game_board,active_user):
    if (game_board[0] == active_user and game_board[1] == active_user and game_board[2] == user): 
      return True
    if (game_board[3] == active_user and game_board[4] == active_user and game_board[5] == active_user):
      return True
    if (game_board[6] == active_user and game_board[7] == active_user and game_board[8] == active_user): 
      return True
    else:
      return False
# Checks to see if any winners via column
def check_win_col(game_board,active_user):
    if (game_board[0] == active_user and game_board[3] == active_user and game_board[6] == active_user): 
      return True
    if (game_board[1] == active_user and game_board[4] == active_user and game_board[7] == active_user): 
      return True
    if (game_board[2] == active_user and game_board[5] == active_user and game_board[8] == active_user): 
      return True
    else:
      return False

# Checks to see if any winners via Diagonal
def check_diagonal(game_board,user):
    if (game_board[0]  == active_user and game_board[4]  == active_user and game_board[8]  == active_user): return True
    if (game_board[2]  == active_user and game_board[4]  == active_user and game_board[6]  == active_user): return True
    else: return False

# Main game for TicTacToe
while counter < 9:
  active_user = current_user(user)
  display_board()
  user_input = input("Please enter a position A1 to A9 or enter \"q\" to quit: ")
  if quit(user_input):
    break
  user_input = int(user_input_transform(user_input))
  if not check_boundary(user_input):
    continue
  user_input = int(user_input) - 1
  if istaken(user_input):
    print("Space already taken. Please try again.")
    continue
  update_board(user_input,active_user)
  if did_win(game_board,active_user):
    display_board()
    print(f'Player {active_user} has won!')
    user_input = input ('Do you want to play again ("y" or "n") ? ')
    if user_input == "y":
      counter = 0
      clear_board(game_board)
    else: break
  user = not user
  counter += 1
  if counter == 9:
    print('Tie!')
    user_input = input ('Do you want to play again ("y" or "n") ? ')
    if user_input == "y":
      counter = 0
      clear_board(game_board)
    else: break
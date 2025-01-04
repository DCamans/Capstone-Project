import random

print("Welcome to Noughts and Crosses!")
print("You are assigned crosses (X) and your opponent is naughts(O)")
print("Given a grid system as showed below, please select an unoccupied grid from 1-9 to make 3 X's in a line")

# I will create a show_grid function which I can use after each iteration of the while loop, making it quite reusable


def show_grid(grid):
    print(f" {grid[0]} | {grid[1]} | {grid[2]} ")
    print(f"---+---+---")
    print(f" {grid[3]} | {grid[4]} | {grid[5]} ")
    print(f"---+---+---")
    print(f" {grid[6]} | {grid[7]} | {grid[8]} ")

# Now another function is created that asks the user for an input and makes sure that input is not taken and that it's a valid input
# This function will not exit the loop until a valid input is selected


def validate_user_input(grid):
    while True:
        move = input("Please enter your move 1-9: ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move)-1
            if grid[move] not in ['O', 'X']:
                return move
            else:
                print("This grid is already taken, try again")
        else:
            print("Please enter a valid input 1-9")

# This function returns a randomly selected free grid which is the computer's response, hence the random module imported earlier
# Creates a list of empty grid references, of which, the computer randomly selects a grid from


def computer_input(grid):
    free_cells = []
    for i in range(9):
        if grid[i] not in ['O', 'X']:
            free_cells.append(i)
    return random.choice(free_cells)

# Now this function will assign victory conditions and check if either player has met them, returning True if they have


def validate_winner(grid, player):
    victory_conditions = [
        [0, 4, 8], [2, 4, 6],
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8]
    ]
    for condition in victory_conditions:
        if all(grid[i] == player for i in condition):
            return True
    return False

# Finally, we are able to start the game! Another function will be created to initialize the game, and perhaps also repeat the game


def start_game():
    grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    show_grid(grid)

    while True:
        # Player move
        player_move = validate_user_input(grid)
        grid[player_move] = 'X'
        show_grid(grid)
        if validate_winner(grid, 'X'):
            print("Congratulations, you win!")
            break

        # Checking for draw
        if all(cell in ['O', 'X'] for cell in grid):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's turn: ")
        grid[computer_input(grid)] = 'O'
        show_grid(grid)
        if validate_winner(grid, 'O'):
            print("Unlucky! Computer wins.")
            break


start_game()

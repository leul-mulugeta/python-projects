from random import randint

# Function to get user input for placing their mark
def get_user_input(player):
    while True:
        try:
            user_input = int(input(f"Please select a position (1-9) to place an '{player}': "))
            # Ensure input is within the valid range
            if user_input < 1 or user_input > 9:
                raise ValueError
            break
        # Ignore invalid inputs and re-prompt user
        except ValueError:
            continue
    return user_input

# Grid placeholders (representing Tic-Tac-Toe board positions)
q = w = e = r = t = y = u = i = o = " "

# Function to display the current Tic-Tac-Toe grid
def show_grid():
    print("   |   |   ")  
    print(f" {q} | {w} | {e} ") 
    print("   |   |   ") 
    print("-----------")
    print("   |   |   ") 
    print(f" {r} | {t} | {y} ") 
    print("   |   |   ") 
    print("-----------")
    print("   |   |   ") 
    print(f" {u} | {i} | {o} ") 
    print("   |   |   ") 

# Function to update the grid with the player's move
def update_grid(user_input, l):
    # Access global grid variables
    global q, w, e, r, t, y, u, i, o

    # Update the correct grid position if it's empty
    if user_input == 1 and q == " ":
        q = l
    elif user_input == 2 and w == " ":
        w = l
    elif user_input == 3 and e == " ":
        e = l
    elif user_input == 4 and r == " ":
        r = l
    elif user_input == 5 and t == " ":
        t = l
    elif user_input == 6 and y == " ":
        y = l
    elif user_input == 7 and u == " ":
        u = l
    elif user_input == 8 and i == " ":
        i = l
    elif user_input == 9 and o == " ":
        o = l

# Function to check if there is a winning combination
def check_win():
    # Check rows, columns, and diagonals for a winning sequence
    if q == w == e and q != " ":
        return True, q
    elif r == t == y and r != " ":
        return True, r
    elif u == i == o and u != " ":
        return True, u
    elif q == r == u and q != " ":
        return True, q
    elif w == t == i and w != " ":
        return True, w
    elif e == y == o and e != " ":
        return True, e
    elif q == t == o and q != " ":
        return True, q
    elif e == t == u and e != " ":
        return True, e
    return False, None

# Function to check if the game is a draw
def check_draw():
    # If all positions are filled and there is no winner, return True (draw)
    if " " not in [q, w, e, r, t, y, u, i, o]:
        return not check_win()[0]  # Ensure there isn't a winner
    return False  # Game is not a draw yet

# Function for playing against the computer
def vs_computer():
    # List to track occupied positions
    used_position = []
    player1 = "X"
    player2 = "O"

    # Display initial empty grid
    show_grid()

    # Continue until there is a winner
    while not check_win()[0]:
        user_input = get_user_input(player1)

        # Ensure the chosen position is not already occupied
        if user_input in used_position:
            continue
        else:
            used_position.append(user_input) # Mark position as used
            update_grid(user_input, player1) # Place player's mark

            # Check for win or draw after player's move
            if check_win()[0]:
                show_grid()
                break
            elif check_draw():
                show_grid()
                break

            # Computer's turn: randomly select an available position
            while True:
                computer = randint(1, 9)
                if computer not in used_position:
                    break
            while True:
                computer = randint(1, 9)
                if computer not in used_position:
                    break
            used_position.append(computer)
            update_grid(computer, player2)
            print(f"Computer placed an 'O' in position {computer}:")
            show_grid()

    # Display result message
    if check_win()[1] == "X":
        print("Player won!")
    elif check_win()[1] == "O":
        print("Computer won!")
    else:
        print("Tie!")

# Function for two-player mode
def vs_player():
    # Track used positions
    used_position = []
    player1 = "X"
    player2 = "O"

    # Show the initial grid
    show_grid()

    # Loop until there's a winner
    while not check_win()[0]:
        # Player 1's turn
        user_input = get_user_input(player1)
        if user_input in used_position:
            continue
        used_position.append(user_input)
        update_grid(user_input, player1)

        # Check for win or draw after Player 1's move
        if check_win()[0]:
            show_grid()
            break
        elif check_draw():
            show_grid()
            break 
        show_grid()

        # Player 2's turn
        while not check_win()[0]:
            user_input = get_user_input(player2)
            if user_input in used_position:
                continue
            used_position.append(user_input)
            update_grid(user_input, player2)

            # Check for win or draw after Player 2's move
            if check_win()[0]:
                show_grid()
                break
            elif check_draw():
                show_grid()
                break
            show_grid()
            break

    # Display result message
    if check_win()[1] == "X":
        print("Player1 won!")
    elif check_win()[1] == "O":
        print("Player2 won!")
    else:
        print("Tie!")

# Function to reset the grid for a new game
def reset():
    global q, w, e, r, t, y, u, i, o
    q = w = e = r = t = y = u = i = o = " "
    
# Main function: game menu
def main():
    print("Welcome to Tic Tac Toe")
    while True:
        # Reset board for a fresh game
        reset()
        user_choice = input("Choose an opponent:\n1. Computer\n2. Player\n")

        # Play against computer
        if user_choice == "1":
            vs_computer()
            answer = input("Play again? (y)es/(n)o ").lower()
            if answer in ["y", "yes"]:
                continue
            elif answer in ["n", "no"]:
                return
            
        # Play against another player
        elif user_choice == "2":
            vs_player()
            answer = input("Play again? (y)es/(n)o ").lower()
            if answer in ["y", "yes"]:
                continue
            elif answer in ["n", "no"]:
                return  
        else:
            continue # Reprompt if invalid input is given

# Run the game
main()
from random import randrange

board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

def display_board(board):
    print("+-------" * 3, "+", sep= "")
    print("|       " * 3, "|", sep= "")
    print("|   " + board[0][0] + "   |   " + board[0][1] + "   |   " + board[0][2] + "   |")
    print("|       " * 3, "|", sep= "")
    print("+-------" * 3, "+", sep= "")
    print("|       " * 3, "|", sep= "")
    print("|   " + board[1][0] + "   |   " + board[1][1] + "   |   " + board[1][2] + "   |")
    print("|       " * 3, "|", sep= "")
    print("+-------" * 3, "+", sep= "")
    print("|       " * 3, "|", sep= "")
    print("|   " + board[2][0] + "   |   " + board[2][1] + "   |   " + board[2][2] + "   |")
    print("|       " * 3, "|", sep= "")
    print("+-------" * 3, "+", sep= "")
    



def enter_move(board):
    while True:
        user_choice = int(input("Enter your selected space: "))
        if user_choice < 1 or user_choice > 9:
            print("Please pick a number from the range of 1 through 9")
            continue
        #convert to string because the elements in the list are a string, so we have
        #to check for a string value in the space
        elif str(user_choice) not in board[0] and str(user_choice) not in board[1] and str(user_choice) not in board[2]:
            print("Sorry that space is already taken. Please select another space.")
            continue
        
        for row in range(0,3):
            for column in range(0,3):
                if(board[row][column] == str(user_choice)):
                    board[row][column] = 'O'
        
        break


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_squares
    free_squares = [] # empty list to implement what squares are empty/taken
    for row in range(0,3):
        for column in range(0,3):
            if(board[row][column] == 'X' or board[row][column] == 'O'):
                pass
            else:
                free_squares.append(([row], [column]))
    print(free_squares)


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    if sign == "O":
        print("Checking to see if you won")
    else:
        print("Checking to see if the computer won")
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign):
        return True
    elif (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign):
        return True
    elif (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign):
        return True
    elif (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign):
        return True
    elif (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign):
        return True
    elif (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
        return True
    elif (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):
        return True
    elif (board[2][0] == sign and board[1][1] == sign and board[0][2] == sign):
        return True
    else:
        print("We don't have a winner yet")



def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        row = randrange(3)
        column = randrange(3)
        if ([row], [column]) not in free_squares:
            continue #redraw a new number if the space is already taken
        else:
            board[row][column] = "X"
            return 
 

number_of_moves = 1 # game always starts with computer X move
human_move = "O"
computer_move = "X"
 
print("Welcome to the Tic-Tac-Toe game!")
display_board(board)

while number_of_moves < 9:
#user's turn  
    enter_move(board)
    number_of_moves += 1
    display_board(board)

    if victory_for(board, human_move) == True:
        print("You won! Woo-hoo!")
        break
    else:
        print("Here is the current list of free spaces.")
        make_list_of_free_fields(board)
        print()
        display_board(board)
    print()
#computer's turn
    print("Computer's turn.")
    draw_move(board)
    number_of_moves += 1
    display_board(board)
    print()
    
    if victory_for(board, computer_move) == True:
        print("You lost! :(")
        break
    else:
        print("Here is the current list of free spaces.")
        make_list_of_free_fields(board)
        print()
        display_board(board)
        
else: print("There is a tie!")

print("Thank you for playing!")

#print("\033[1;32m This text is Bright Green  \n")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKGREEN}Welcome to Gato Game{bcolors.ENDC}")
name = input("What is your name?: ").capitalize().strip()
board = ["  " for i in range(9)]

def get_colored_icon(icon):
    if icon == "X":
        return f"{bcolors.WARNING}{icon}{bcolors.ENDC}"
    elif icon == "O":
        return f"{bcolors.OKCYAN}{icon}{bcolors.ENDC}"
    else:
        return icon

def print_board(): #Juego ti ta to
    row1 = f"| {get_colored_icon(board[0])} | {get_colored_icon(board[1])} | {get_colored_icon(board[2])} |"
    row2 = f"| {get_colored_icon(board[3])} | {get_colored_icon(board[4])} | {get_colored_icon(board[5])} |"
    row3 = f"| {get_colored_icon(board[6])} | {get_colored_icon(board[7])} | {get_colored_icon(board[8])} |"

    print("")
    print(row1)
    print(row2) 
    print(row3)
    print("")

def player_move(icon):
    if icon == "X":
        number = name
        color = bcolors.WARNING # set color for "X"
    elif icon == "O":
        number = 2
        color = bcolors.OKCYAN # set color for "O"

    print(f"{color}Your turn player {number}. {icon}{bcolors.ENDC}") # escoge el turno del jugador colored output
    #print("Let's Goo!! {}".format(number, color + icon + bcolors.ENDC))# escoge el turno del jugador

    while True: #Pokayoke solo numeros
        user_input = input("Enter your move (1-9): ")
        if user_input.isdigit():
            choice = int(user_input)
            if 1<= choice <=9:
                break
        else:
            print(f"{bcolors.FAIL}Error: Please enter a number between 1 & 9.{bcolors.ENDC}") #error handdeler

    if board[choice -1] == "  ":
        board[choice -1 ] = icon
    else:
        print()
        print("{} That space is Busy!".format(number))

def win(icon): #  win calculation
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board [5] == icon) or \
       (board[6] == icon and board[7] == icon and board [8] == icon) or \
       (board[0] == icon and board[3] == icon and board [6] == icon) or \
       (board[1] == icon and board[4] == icon and board [7] == icon) or \
       (board[2] == icon and board[5] == icon and board [8] == icon) or \
       (board[3] == icon and board[6] == icon and board [8] == icon) or \
       (board[0] == icon and board[4] == icon and board [8] == icon) or \
       (board[2] == icon and board[4] == icon and board [6] == icon):
        return True
    else:
        return False

def draw():
    if "  " not in board:
        return True
    else:
        return False

while True: #actual aplication
    print("Lets go {}".format(name))
    print_board()
    player_move("X")
    print_board()
    color = bcolors.OKBLUE # set color for "X"
    if win("X"): # x win calculation
        print_board()
        print("{}!, Contrats you Win".format(name))
        break
    elif draw(): #x draw calulaction
        #print("Its a draw!!")
        print(f"{bcolors.OKGREEN}Its a draw!!{bcolors.ENDC}")
        print_board()
        break

    player_move("O")
    if win("O"):# O win calculation
        print_board()
        print("{}!, Contrats you Win".format(2))
        break
    elif draw():#O draw calulaction
        print("Its a draw!!")
        print_board()
        break

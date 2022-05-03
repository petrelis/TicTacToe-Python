positions = [[0,0,0], 
             [0,0,0],
             [0,0,0]]

#Prints array values on a board
def Display(positions):

    for i in range(len(positions)):
        for j in range(len(positions[i])):
            if positions[i][j] != 0:
                print(" " + str(positions[i][j]) + " ", end="")
            else: print("   ", end="")
            if j != len(positions[i])-1: print("|", end="")
            j += 1
        if i != len(positions)-1:
            print()
            print("---+---+---")
        i += 1
    print()

#Asks for player input and changes array value accordingly
def PlaceXO(index):
    print("Choose a position(1-" + str(len(positions) * len(positions[0])) + "): ", end="")
    x = getInput()
    while x > len(positions) * len(positions[0]) or x < 1:
        print("Choose a valid position(1-" + str(len(positions) * len(positions[0])) + ")", end=": ")
        x = getInput()
    move=int(x)-1
        
    move_y = int(move / 3)
    move_x = move % 3
    while positions[move_y][move_x] == "X" or positions[move_y][move_x] == "O" :
        print("this position is taken, please enter a new one: ", end="")
        move = getInput() - 1
        move_y = int(move / 3)
        move_x = move % 3
    if index % 2 == 0:
        positions[move_y][move_x] = "X"
    else: positions[move_y][move_x]= "O"

#checks for both player wins. If game is not won calls PlaceXO and Display methods and checks for wins again
def Win(positions):
    index=0
    won = False
    while True:
        if index > 8:
            print("Draw!")
            break
        if won == True: break
        PlaceXO(index)
        index += 1
        Display(positions)
        x_count_d=0
        x_count_d_back=0
        o_count_d=0
        o_count_d_back=0
        for i in range(len(positions)):
            x_count_h=0
            o_count_h=0
            x_count_v=0
            o_count_v=0
            
            #checks for diagonal X wins
            if positions[i][i] == "X":
                x_count_d = x_count_d + 1
                if x_count_d == len(positions[0]): 
                    won = True
                    print("X won!")
                    break
            
            #checks for backwards diagonal X wins
            n=len(positions[0])-i-1
            if positions[i][n] == "X":
                x_count_d_back = x_count_d_back + 1
                if x_count_d_back == len(positions[0]): 
                    won = True
                    print("X won!")
                    break

            #checks for diagonal O wins
            if positions[i][i] == "O":
                o_count_d = o_count_d + 1
                if o_count_d == len(positions[0]): 
                    won = True
                    print("O won!")
                    break
            
            #checks for backwards diagonal O wins
            n=len(positions[0])-i-1
            if positions[i][n] == "O":
                o_count_d_back = o_count_d_back + 1
                if o_count_d_back == len(positions[0]): 
                    won = True
                    print("O won!")
                    break

            for j in range(len(positions[0])):
                
                #checks for horizontal X wins
                if positions[i][j] == "X":
                    x_count_h = x_count_h + 1
                    if x_count_h == len(positions[0]): 
                        won = True
                        print("X won!")
                        break

                #checks for horizontal O wins
                if positions[i][j] == "O":
                    o_count_h = o_count_h + 1
                    if o_count_h == len(positions[0]): 
                        won = True
                        print("O won!")
                        break

                #checks for vertical X wins
                if positions[j][i] == "X":
                    x_count_v = x_count_v + 1
                    if x_count_v == len(positions[0]): 
                        won = True
                        print("X won!")
                        break

                #checks for vertical O wins
                if positions[j][i] == "O":
                    o_count_v = o_count_v + 1
                    if o_count_v == len(positions[0]): 
                        won = True
                        print("O won!")
                        break    
            
            if won == True: break

#checks if input is a number
def getInput():
    value = input()
    while not value.isnumeric():
        value = input("Position must be a valid number, try again: ")
        if value.isnumeric():
            if int(value) < 1 or int(value) > 9:
                value = "not valid"
        else:
            value = "not valid"
    return int(value)

#clears all array values
def clear():
    for i in range(len(positions)):
        for j in range(len(positions[0])):
            positions[i][j] = 0


#main
playagain = "y"
while playagain == "y":
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()
    clear()
    Win(positions)
    playagain = input("Play again y/n: ")
    

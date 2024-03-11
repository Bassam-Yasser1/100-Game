# File: CS112_A1_T2_1_20230089
# Purpose: "100 game" Each player picks a number from 1 to 10 and the player that reaches 100 wins
# Author: Bassam Yasser Mohamed
# ID: 20230089

print("Welcome to 100 game")
print("Each player picks a number from 1 to 10\nThe player that reaches 100 wins\n") # Explaining the game to the players
print("Sum = 0") # Displaying initial game status

sum = 0

while True: # The loop keeps looping until some player wins, and then we will break the loop
    while True: # To Take the move from Player1, this loop keeps looping until he enters a valid input (numeric)
        try:
            move = int(input("Player 1: Please pick a number: "))

        except ValueError:
            print("Invalid input, Please enter a number")
            continue
        break

    while move not in range (1,11): # This loop keeps looping until he enters a valid input (in the allowed range)
        print("Number is not valid")
        while True:
            try:
                move = int(input("Player 1: Please pick a number: "))

            except ValueError:
                print("Invalid input, Please enter a number")
                continue
            break

    sum += move # After taking Player 1's move, we add it to sum

    while sum > 100: # To check if sum>100 and if so the move will be rejected and the player makes another move
        sum -= move
        move = int(input("Please pick a valid number: "))
        sum += move

    print("Sum = " + str(sum)) # Updating game status

    if sum == 100: #check if player1 wins
        print("Player 1 wins")
        break

    while True: # To Take the move from Player2, this loop keeps looping until he enters a valid input (numeric)
        try:
            move = int(input("Player 2: Please pick a number: "))

        except ValueError:
            print("Invalid input, Please enter a number")
            continue
        break

    while move not in range (1,11) : # This loop keeps looping until he enters a valid input (in the allowed range)
        print("Number is not valid")
        while True:
            try:
                move = int(input("Player 2: Please pick a number: "))

            except ValueError:
                print("Invalid input, Please enter a number")
                continue
            break

    sum += move # After taking Player 2's move, we add it to sum

    while sum > 100: # To check if sum>100 and if so the move will be rejected and the player makes another move
        sum -= move
        move = int(input("Please pick a valid number: "))
        sum += move

    print("Sum = " + str(sum)) # Updating game status

    if sum == 100: #check if player2 wins
        print("Player 2 wins")
        break

print("Thanks for Playing!")
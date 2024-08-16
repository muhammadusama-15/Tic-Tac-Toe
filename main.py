#Tic Tac Toe Game 

#Importing player class from player.py
from player import Player

#Importing random module for playing against computer
from random import randint
import time

#Defining Game Layout
game_layout = [
               ["_","_","_"],
               ["_","_","_"],
               ["_","_","_"]
               ]

def print_game_layout():
    for row in game_layout:
        print(row[0],"|",row[1],"|",row[2])


#Welcoming the players
print("-------------------------------------------Tic Tac Toe-------------------------------------------")

#Getting hold of the players
p1_name = input("Enter the name of first player: ")
p2_name = input("Enter the name of second player or 'computer' for playing against Computer: ")
player_1 = Player(p1_name)
player_2 = Player(p2_name)

#Assigning symbols to the players
player_1.symbol = "O"
player_2.symbol = "X"

print_game_layout()
#Game Behaviour
game_is_on = True
while game_is_on:
    #Player 1 input
    if "_" in game_layout[0] or "_" in game_layout[1] or "_" in game_layout[2]:
        while True:
            p1_turn = input(f"Where does {player_1.name} want to put {player_1.symbol}. Write 'row,column'e.g.'1,1': ")
            player_1.put_mark(game=game_layout, coordinates=p1_turn)

            #If user/computer wastes the turn, they will be allowed to do it again.
            if player_1.marked == True:
                break
            else:
                continue

        #Printing game layout for better user experience.
        print_game_layout()

        #Checking if a player has won.
        p1_won = player_1.is_winner(game=game_layout)
        if p1_won:
            print(f"{player_1.name} won.")
            game_is_on = False
            break

    #Player 2 input
    if "_" in game_layout[0] or "_" in game_layout[1] or "_" in game_layout[2]:
        while True:
            if p2_name.lower() == "computer":
                print(f"{player_2.name} is thinking...")
                time.sleep(1) #For good user experience
                p2_turn = f"{randint(1,3)},{randint(1,3)}"
            else:
                p2_turn = input(f"Where does {player_2.name} want to put {player_2.symbol}. Write 'row,column'e.g.'1,1': ")
            player_2.put_mark(game=game_layout, coordinates=p2_turn)
            #If user/computer wastes the turn, they will be allowed to do it again.
            if player_2.marked == True:
                break
            else:
                continue

        #Printing game layout for better user experience.
        print_game_layout()

        #Checking if a player has won.
        p2_won = player_2.is_winner(game=game_layout)
        if p2_won:
            print(f"{player_2.name} won.")
            game_is_on = False
            break

    else:
        print("Match Draw")
        game_is_on = False


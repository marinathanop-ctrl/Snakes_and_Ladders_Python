#Marina Thanopoulou AM5802

# I import random for the die and for the choice of the first player.
import random

# I use dictionaries for the ladders and the snakes that this particular game will have (in this case, the numbers are the exact ones found in the reference image from the exercise).
ladders = {
    1:38,
    4:14,
    8:30,
    21:42,
    28:76,
    50:67,
    71:91,
    80:99
}

snakes = {
    36:6,
    32:10,
    62:18,
    88:24,
    48:26,
    95:56,
    97:78
}

# I have divided the program into six different functions.

# This one is responsible for the action taken if the player ends up in a position where the head of a snake is placed. 
# Afterwards, the function returns the new position of the player that lost places due to the snake. It uses the snake dictionary to check the position.

def oops_snakes(placement):

    if placement in snakes:
        print(f"You are unlucky! Snake from {placement} to {snakes[placement]}")
        return snakes[placement]
    
    return placement

# On the other hand, this function does the same thing but for the ladders instead. 
# So, it operates by the use of the ladders dictionary and returns the final position of the player involved.

def yay_ladders(placement):

    if placement in ladders:
        print(f"You are lucky! Ladder from {placement} to {ladders[placement]}")
        return ladders[placement]
    return placement

# This next function is responsible for the saving of the game in a file. It uses the theory of files in order to create a file that will host the data of the game. 
# I am using the method f.write to write the data needed to load the game inside said file.

def save_the_game(players, placements, current_player):

    with open("savedgame.txt", "w", encoding="utf-8") as f:
        f.write(str(len(players)) + "\n" )
        for i in range(len(players)): 
            f.write(f"{players[i]} {placements[i]} \n")
        f.write(str(current_player) + "\n")
    print("Game interrupted successfully. Status is saved in file savedgame.txt")

#This function is responsible for the loading of the previous game, if there is one. If the file indeed exists, the function uses file theory and f.readlines in order to take the data from the file and be able to continue the game. 
#If the file however does not exist, the function prints an error message and starts a new game by calling on the next function.

def load_the_game():

    try:
        with open("savedgame.txt", "r", encoding="utf-8") as f:
            data = f.readlines()
        player_num = int(data[0].strip())
        players = []
        placements = []
        for x in range(1, player_num + 1):
            parts = data[x].strip().split()
            players.append(parts[0])
            placements.append(int(parts[1]))
        
        current = int(data[-1].strip())
        print("Loaded saved game:")

        for y in range(player_num):
            print (f"{players[y]} is at square {placements[y]}")
        
        print(f"Next player is {players[current]}")
        return players, placements, current
    
    except FileNotFoundError:
        print("No saved game found. Starting a new game...")
        return play_new_game()

# This function is the one that basically collects all the data from the user and selects a player to start the game.
# It selects the number of players and their names. It also gives each player their position which is zero.

def play_new_game():

    player_num = int(input("Please enter a number of players: "))
    players = []
    placements = [0] * player_num

    for z in range(player_num):
        player_name = input(f"Player {z + 1}, please enter your name: ")
        players.append(player_name)
    
    first_player = random.randint(0, player_num - 1 )
    print(f"{players[first_player]}, you are randomly selected to start first.")

    return players, placements, first_player

# This is the final function of the program and perhaps the most important. 
# Firstly, I ask the user whether or not he wants to continue his previous game. Depending on his answer, the function either calls the load_the_game function or the play_new_game function. 
# I use the while loop in order to repeat the print of positions, the die roll and the check of the placements.

def play_snakes_and_ladders():

    choose = input("Please enter 'L' or 'l' to continue last saved game, or any other input to start a new game: ")
    if choose.lower() == "l":
        players, placements, current = load_the_game()
    else:
        players, placements, current = play_new_game()
    player_num = len(players)

    while True:
        player = players[current]
        print("\nPositions: " )
        for w in range(player_num):
            print(f"{players[w]} at square {placements[w]}")
            
        next = input(f"{player}, hit ENTER to roll the die, or 'S' to save current game and exit: ")
        if next.lower() == 's':
            save_the_game(players, placements, current)
            break
        die = random.randint(1, 6)
        print(f"{player} rolled {die}")

        new_place = placements[current] + die
        if new_place > 100:
            print(f"{player}, the die takes you outside the board, so you stay at {placements[current]}")
        elif new_place == 100:
            print(f"{player}, congratulatons! You are the first to land on square 100 and you win the game!")
            break
        else:
            placements[current] = new_place
            placements[current] = yay_ladders(placements[current])
            placements[current] = oops_snakes(placements[current])
        
        current = (current + 1) % player_num

play_snakes_and_ladders()
# Snakes_and_Ladders_Python
This is the classic game of snakes and ladders written in Python.
It was asked as a university project and this is a polished revision of it.
The program uses import random for the die and the choice of who is the first player.
Then I use dictionaries for the ladders and the snakes (these stay the same for the game).
Then, the code is divided into six functions.
oops_snakes is the function that takes the player to the end of the snake tail when the tile the players falls on is the head of a snake
yay_ladders on the other hand does the exact opposite and has the player climbing up the board
save_the_game is used so we can save the game currently being played in a file that is created at that moment by our code, inside the current file (there was at first a difference in where it was saved between Obuntu and Windows 11 but it has been resolved)
load_the_game finds that file and reads it so the game can be resumed, FileNotFoundError was taken into consideration so if you didn't save a game the code will start a new game for you after telling you about the previous game not being found.
play_new_game collects the data from the user, such as how many players are there and what are ther names, and it gives the starting position of the players which is tile nummber 0, this function also uses random.randit to select the player that will roll the die first
Last but not least, play_snakes_and_ladders is the function that binds all the above together, if the user types l the function calls on load_the_game to find the previous game and continue on with it and when there isn't a previous game the function calls play_new_game and then I use a for loop to re-print every message needed accordingly at each round

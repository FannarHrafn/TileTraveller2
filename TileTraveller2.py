# Fannar Hrafn Haraldsson
# Tile Traveller
# Fannar Hrafn Haraldsson
# Tile Traveller
# https://github.com/FannarHrafn/TileTraveller2

# grid contains x and o because I initially planned to print out the grid
# but project doesn't want it, but its easy to add now in the future
import random

grid = [
    [["(E)ast or (S)outh", "x"], ["(E)ast or (W)est", "x"], ["(S)outh or (W)est", "x"]],
    [["(N)orth or (E)ast or (S)outh", "x"], ["(S)outh or (W)est", "x"], ["(N)orth or (S)outh", "x"]],
    [["(N)orth", "o"], ["(N)orth", "x"], ["(N)orth", "x"]]
]


# fetches string of possible paths
def travel_options(curr_pos, grid):
    return grid[curr_pos[0]][curr_pos[1]][0]


# prints string of valid directions
def travel_printer(travel_string):
    return print("You can travel: " + travel_string + ".")


# ask user for direction until user inputs a valid direction
def get_direction(travel_string):
    while True:
        #random input from list
        print("Direction: ")
        direction = random.choice(directions_list)
        if direction.upper() in travel_string:
            return direction.upper()
        else:
            print("Not a valid direction!")
            travel_printer(travel_string)


# moves position to new position and returns the new pos and grid with changes
def new_pos(curr_pos, direction, grid):
    # remove old position
    grid[curr_pos[0]][curr_pos[1]][1] = "x"
    # change positional list according to direction
    # no need to test if we're going out of bounds as we know
    # that only legal moves make it in here because of get_direction checking them
    if direction == "N":
        curr_pos[0] -= 1
    elif direction == "S":
        curr_pos[0] += 1
    elif direction == "E":
        curr_pos[1] += 1
    elif direction == "W":
        curr_pos[1] -= 1
    # mark new position
    grid[curr_pos[0]][curr_pos[1]][1] = "o"
    return curr_pos, grid


def coin_giver(grid,curr_pos,coins):
    #list of all locations with coin levers
    coin_pos_list =  [grid[1][0], grid[1][1], grid[0][1], grid[1][2]]
    #check if user is in of these locations
    if grid[curr_pos[0]][curr_pos[1]] in coin_pos_list:
        #random input from list
        print("Pull a lever (y/n): ")
        user_input = random.choice(y_or_n_list)
        #give 1 coin if yes else just return with nothing gained
        if user_input == "y" or user_input == "Y":
            coins += 1
            print("You received 1 coin, your total is now "+str(coins)+".")
            return coins
        else:
            return coins
    else:
        return coins

def play_again():
    #reset curr_pos and coins back to starting values
    return [2,0], 0


# starting position
curr_pos = [2, 0]
coins = 0
moves = 0
#get random seed
user_seed = int(input("Input seed: "))
random.seed(user_seed)
y_or_n_list = ["y","n"]
directions_list = ["N","S","W","E"]

while True:
    #check for coin lever
    coins  = coin_giver(grid,curr_pos,coins)
    # get string of possible paths
    travel_string = travel_options(curr_pos, grid)
    # print paths
    travel_printer(travel_string)
    # get direction from user
    direction = get_direction(travel_string)
    # make a new curr_pos and change the position on the grid
    curr_pos, grid = new_pos(curr_pos, direction, grid)
    if grid[curr_pos[0]][curr_pos[1]] == grid[2][2]:
        print("Victory! Total coins " + str(coins)+ ". Moves " + str(moves) + ".")
        print("Play again (y/n): ")
        user_input = random.choice(y_or_n_list)
        if user_input == "y" or user_input == "Y":
            curr_pos, coins = play_again()
        else:
            break
    moves +=1

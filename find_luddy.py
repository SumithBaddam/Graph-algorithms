#!/usr/local/bin/python3
# find_luddy.py : a simple maze solver


import sys
import json

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
    moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

#Get direction from previous and currenet positions
def getDirectionsUtil(prev_move, new_move):
    if(new_move[1] == prev_move[1] + 1):
        return 'E'
    elif(new_move[0] == prev_move[0] + 1):
        return 'S'
    elif(new_move[1] == prev_move[1] - 1):
        return 'W'
    elif(new_move[0] == prev_move[0] - 1):
        return 'N'

def getDirections(path, final_loc):
    directions = []
    for i in range(len(path)-1):
        prev_move = path[i]
        new_move = path[i+1]
        #print(prev_move, new_move)
        directions.append(getDirectionsUtil(prev_move, new_move))
    directions.append(getDirectionsUtil(new_move, final_loc))
    return ''.join(directions)

# Perform search on the map
def search1(IUB_map):
    # Find my start position
    #print(IUB_map)
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    path = []
    visited = [[0 for col_i in range(len(IUB_map[0]))] for row_i in range(len(IUB_map))]
    pred = [[(-1,-1) for col_i in range(len(IUB_map[0]))] for row_i in range(len(IUB_map))]
    q = [(you_loc, 0)]
    #fringe=[(you_loc,0)]
    #print(you_loc, q, visited)
    while q:
        (curr_move, curr_dist) = q.pop()
        visited[curr_move[0]][curr_move[1]] = 1
        for move in moves(IUB_map, *curr_move):
            #print(move)
            if IUB_map[move[0]][move[1]]=="@":
                pred[move[0]][move[1]] = curr_move
                #print(pred)
                return (curr_dist+1, you_loc, move, pred)
            else:
                if(visited[move[0]][move[1]] == 0):
                    #print(curr_move, move, direction(curr_move, move))
                    #path.append(direction(curr_move, move))
                    pred[move[0]][move[1]] = curr_move
                    q.append((move, curr_dist + 1))
    return -1,1-1,-1,-1

#Print the path from the predecessor list
def printPath(initial_loc, final_loc, pred):
    final = final_loc
    path = []
    while(pred[final_loc[0]][final_loc[1]] != (-1, -1)):
        path.append(pred[final_loc[0]][final_loc[1]])
        final_loc = pred[final_loc[0]][final_loc[1]]
    directions = getDirections(path[::-1], final)
    return directions

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])

    #print(IUB_map)
    #IUB_map = IUB_map[:-1]
    print("Shhhh... quiet while I navigate!")
    distance, initial_loc, final_loc, pred = search1(IUB_map)
    if(distance == -1):
        print('Inf')
    else:
        directions = printPath(initial_loc, final_loc, pred)
        print("Here's the solution I found:")
        print(distance, directions)

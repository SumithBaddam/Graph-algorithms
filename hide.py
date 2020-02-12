#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : [Sumith Reddi Baddam - srbaddam]
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys
import time
# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors(board):
    return [ add_friend(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.' ]

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 

def checkFriendCanSee(board, i, j):
    c = 0
    for l in range(len(board[0])):
        if(board[i][l] == 'F'):
            c = c + 1
        elif(board[i][l] == '&' and c>0):
            c = c - 1
        if(c > 1):
            return False
    c = 0
    for k in range(len(board)):
        if(board[k][j] == 'F'):
            c = c + 1
        elif(board[k][j] == '&' and c > 0):
            c = c - 1
        if(c > 1):
            return False
    return True


def isBoardValid(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 'F'):
                if(not checkFriendCanSee(board, i, j)):
                    return False
    return True

'''
# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    visited = []
    while(len(fringe) > 0):
        board = fringe.pop()
        for s in successors(board):
            if(s not in visited):
                if(isBoardValid(s)):
                    if(is_goal(s)):
                        return(s)

                    if(s not in fringe):
                        fringe.append(s)

                visited.append(board)
        
    return False
'''

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    visited = []
    while(len(fringe) > 0):
        board = fringe.pop()
        for s in successors(board):
            if(s not in visited):
                if(isBoardValid(s)):
                    if(is_goal(s)):
                        return(s)

                    #if(s not in fringe):
                    fringe.append(s)

        visited.append(board)

    return False

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    start_time = time.clock()
    # This is K, the number of friends
    K = int(sys.argv[2])
    #IUB_map = IUB_map[:-1]
    #print(IUB_map)
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")
    #print (time.clock() - start_time, "seconds")

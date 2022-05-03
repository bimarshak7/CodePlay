#!/bin/python
grid = [[1, 0, 0, 6, 0, 0, 5, 0, 0],
       [9, 0, 0, 0, 0, 2, 0, 0, 0],
        [6, 3, 0, 9, 0, 0, 0, 0, 7],
        [2, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 7, 3, 0, 0, 1, 0, 0],
        [0, 0, 8, 0, 7, 0, 0, 0, 0],
        [0, 4, 0, 0, 6, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 5, 6, 0, 4],
        [5, 9, 0, 0, 0, 0, 8, 2, 0]]

#grid = np.zeros(shape=(9,9), dtype=int)
def disp(grid):
    line = "-|"+"-"*28+"|-"
    for i in range(9):
        if i%3==0:print(line)
        for j in range(9):
            if j%3==0: print(" |",end="  ")
            print(grid[i][j],end=" ")
        print("|")
    print(line)


def find_empty(grid):
    ''' Find the next empty cell in the grid '''
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return (i,j)
    return None


def valid(board,pos,num):
    #check in the row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1]!=i:
            return False
    #check column
    for i in range(9):
        if board[i][pos[1]] ==num and pos[0]!=i:
            return False

    #check subgrid
    subX = pos[1]//3
    subY = pos[0]//3
    
    for i in range(subY*3,subY*3+3):
        for j in range(subX*3, subX*3+3):
            if grid[i][j]==num and pos != (i,j):
                return False
    
    return True #valid case


def solve(grid):
    find = find_empty(grid)
    if not find: # base case, if there are no more empty space, exit the recursive call
        return True
    row,col = find
    for i in range(1,10): #try all numbers (0-9) in the empty cell found
        if valid(grid,find,i): #check if the assigned number is valid for current board state
            grid[row][col] = i

            if solve(grid): #solve puzzle recursively
                return True
            grid[row][col] = 0 # if  
    return False 

disp(grid) #print board before solving
solve(grid) # solve the puzzle

#check if the puzzle is solved or not (if there are still empty space, it's wasn't solved)
if not find_empty(grid): 
    msg = "Hooray!!! Here is the solution."
else:
    msg = "Sorry!!! This soduku is not solvable."

print("*"*32)
print(msg)
print("*"*32)

if not find_empty(grid):disp(grid) # display solved board (only if it was solved)

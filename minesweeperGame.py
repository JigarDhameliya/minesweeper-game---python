#Jigar M Dhameliya
#101177665
#Assignment_05
#Creating a minesweeper game


import random

GRID_SIZE = 7  #global variable to decide our grid size
MINE_CHANCE = 10   

#a mine bomb class that creates a bomb
class Bomb:
    def __init__(self):
        self.mine = ""
        self.checked = False    

#this function randomly places a mine in the grid
def placeMines():
    grid = []
    for i in range (GRID_SIZE):
        subGrid = []
        for j in range (GRID_SIZE):
            subGrid.append(Bomb())
        grid.append(subGrid)
    for k in range (GRID_SIZE):
        for l in range (GRID_SIZE):
            randomNum = random.randint(1,MINE_CHANCE)   #1 in 10 mine chance 
            if randomNum == 3:    #any random number, i took 3
                grid[k][l].mine = "x"   #giving the element a value of mine
    return grid
#print(placeMines())


#this function makes Board for player, it should be a 2D list
def makeBoard():
    final = []
    for l in range (GRID_SIZE):
        subLis = []
        for m in range (GRID_SIZE): 
            subLis.append("#")
        final.append(subLis)
    return final
#print(makeBoard())


#this functions displays the 2D players board into a readable format
def showBoard(lis):
    for i in range (len(lis)):
        if i == 0:   #prints the first line (  |0)
            print(" |",end="")
            print(i,end="")
        else:
            print(i,end="")     #prints rest of all things (1234...)
    print()
    print("-"*(len(lis)+3))
    for j in range (len(lis)):
        if j != 0:
            print()
        print(j,end="")    #prints the column indices
        print("|",end="")
        for k in range (len(lis)):
            print(lis[j][k],end = "")    #fills the table with all other informations
    print()
#showBoard(makeBoard())


#counts all the unrevealed cells
def countHiddenCell(lis):
    sum = 0
    for i in range (len(lis)):
        for j in range (len(lis)):
            if lis[i][j] == "#":   #if unrevealed the add 1
                sum +=1
    return sum
#print(countHiddenCell(makeBoard()))


#this function counts the number of mines in the grid
def countAllMines(lis):
    numMines = 0
    for i in range (len(lis)):
        for j in range (len(lis)):
            if lis[i][j].mine == "x":    #if it is a mine then add 1
                numMines += 1
    return numMines
#print(countAllMines(placeMines()))


#an additional function to reduce more typing
#this function checks if the given parameters are in range or not 
def inGrid(x,y):
    if x >= 0 and x <= (GRID_SIZE-1) and y >= 0 and y<= (GRID_SIZE-1):
        return True 
    return False 


#function tells whether there is a mine at given param or not
def isMineAt(lis,x,y):
    if inGrid(x,y):  #input validation
        if lis[x][y].mine == "x":  #if mine 
            return True
    return False
#print(isMineAt(placeMines(),2,1))
#validate the input


#a function to count the adjacent mines 
#we have to check if there is a mine around a given cell
#we see the 8 cells around the given cell  (not always 8
#we don't check on that very cell. Only check on adjacent cells
def countAdjacentMines(lis,x,y):
    adjMines = 0
    if inGrid((x-1),(y-1)):   #input validation needed to check because all cells won't have 8 adjacent cells (eg, 0,0)
        if isMineAt(lis,(x-1),(y-1)):   #if there is a mine
            adjMines += 1    #add 1
    if inGrid((x-1),(y)):
        if isMineAt(lis,(x-1),(y)): 
            adjMines += 1
    if inGrid((x-1),(y+1)):
        if isMineAt(lis,(x-1),(y+1)): 
            adjMines += 1
    if inGrid((x),(y-1)):
        if isMineAt(lis,(x),(y-1)):  
            adjMines += 1
    if inGrid((x),(y+1)):
        if isMineAt(lis,(x),(y+1)): 
            adjMines += 1
    if inGrid((x+1),(y-1)):
        if isMineAt(lis,(x+1),(y-1)): 
            adjMines += 1
    if inGrid((x+1),(y)):
        if isMineAt(lis,(x+1),(y)): 
            adjMines += 1
    if inGrid((x+1),(y+1)):
        if isMineAt(lis,(x+1),(y+1)): 
            adjMines += 1
    return adjMines
#print(countAdjacentMines(placeMines(),0,0))
#print(countAdjacentMines([["x",2,3,4],[4,5,6,7],[7,"x",9,"x"],[1,2,"x",8]],1,2))
        
#PART3
#this function replaces the number of adjacent mines in place of the cell provided
#if 0 then check all the adjacent cells untill they are > 0 
#a recursive function 
def reveal(minefield,playerGrid,x,y):
        if not inGrid(x,y):   #base case / input validation
            return
        if minefield[x][y].checked:     #base case / if the place already checked then return 
            return
        if isMineAt(minefield,x,y):     #base case / if we find a mine then also return, initially false
            return
        minefield[x][y].checked = True  #re assigning to remove recursion 
        if countAdjacentMines(minefield,x,y) > 0:   #base case / if adj. mines > 0 then return 
            playerGrid[x].pop(y)   #replace with number
            playerGrid[x].insert(y,countAdjacentMines(minefield,x,y))
            return
        if countAdjacentMines(minefield,x,y) == 0:  
            playerGrid[x].pop(y)    #replace with " "
            playerGrid[x].insert(y," ")
        for (ele1,ele2) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,-1)]:  #recursive case 
            reveal(minefield,playerGrid,(x+ele1),(y+ele2))

#one other helper function that creates a playerGrid when the player loses
def mineGrid(minefield,playerGrid):
    for i in range (len(minefield)):
        for j in range (len(minefield)):
            if isMineAt(minefield,i,j):
                playerGrid[i][j] = "X"   #replacing all the mines with "X" in the current playerGrid
    showBoard(playerGrid)   #prints the updated grid
#mineGrid()


#PART2

def main():
    minefield = placeMines()   #initializing minefield and playerGrid
    playerGrid = makeBoard()
    print()
    print("Welcome to my Minesweeper® game!")
    print("The best game to play in this self-quarantine!")
    print()
    decision = input("Would you like to play game today? (yes/no) ")
    while decision != "yes" and decision != "no":
        decision = input("Would you like to play game today? (yes/no) ")
    if decision == "yes":
        benefit = input("Do you want a reference by knowing the number of mines earlier ? ")
        while benefit != "yes" and benefit != "no":
            benefit = input("Do you want to make game easy by knowing the number of mines earlier ? ")
        if benefit == "yes":
            print(f"The number of Bombs in the minefield are {countAllMines(minefield)} ")
        print()
        showBoard(playerGrid)
        print()
        done = True 
        while done:  #try and except to handle bad inputs
            try:
                userInput = input("Enter a cell value you think mine isn't present (row,col): ")
                x = int(userInput.split(",")[0])
                y = int(userInput.split(",")[1])
                done = False
                break
            except ValueError:   #if strings then except 
                done = True
            except IndexError:  #if big or small or single inputs 
                done = True
        while not isMineAt(minefield,x,y):  #only starts if it is not mine
            reveal(minefield,playerGrid,x,y)
            print()
            showBoard(playerGrid)
            print()
            if countHiddenCell(playerGrid) == countAllMines(minefield):   #if num of mines is equal to unrevealed cells 
                print("You Won!")
                print()
                print("Ok, Have a great day ahead! and yes, stay home, stay safe, stay healthy ")
                print("Bye-Bye")
                print()
                return
            else:
                done = True 
                while done:
                    try:
                        userInput = input("Enter a cell value you think mine isn't present (row,col): ")
                        x = int(userInput.split(",")[0])
                        y = int(userInput.split(",")[1])
                        done = False
                        break
                    except ValueError:
                        done = True
                    except IndexError:
                        done = True
        print()
        mineGrid(minefield,playerGrid)    #player lost so print the grid with all mines revealed
        print("You lose!")
    if decision == "no" or True:
        print()
        print("Ok, Have a great day ahead! and yes, stay home, stay safe, stay healthy ")
        print("Bye-Bye")
        print()
main()
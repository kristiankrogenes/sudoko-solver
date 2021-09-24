import random as r
import copy

sudokoPuzzles = ["290500007700000400004738012902003064800050070500067200309004005000080700087005109",
                 "080020000040500320020309046600090004000640501134050700360004002407230600000700450",
                 "608730000200000460000064820080005701900618004031000080860200039050000100100456200",
                 "902040560000009000061250470040030102600480090003070080500008000306500947100360005",
                 "020001630090500400806049002900005701000900300352076800009004506080050000045600018",
                 "034060901700012680080009000023050790007020005500078030010590000000000413078130020",
                 "020604030450100206600005100004003000095201380200500907510000603807352000000000058",
                 "032054900090001004080700031005600027800070000270140005000210300018907652603000000",
                 "009000700080034065500027001400380096300400017908006000610009308023501070000060040",
                 "710480060090050070004030908000040090080300020630208045000500000027001059560970201",
                 "040085701950700800080006400370002000002008170600007082809023500400800010001050208",
                 "050800300001040860308010002085230600003080007020090083560170498807400000000050700"]

def getRandomStringPuzzle():
    randNum = r.randint(0, len(sudokoPuzzles)-1)
    return sudokoPuzzles[randNum]

def stringToArray(string):
    
    puzzleArray = []

    index = 0

    for i in range(9):
        
        row = []
        
        for j in range(9):
            row.append(int(string[index]))
            index += 1

        puzzleArray.append(row)

    return puzzleArray

def generateEditableValues(puzzle):
    
    editableValues = []
    
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                editableValues.append([0, i, j])
        
    return editableValues

def isValidValue(num, row, col, puzzle):
    
    for i in range(9):
        if num == puzzle[row][i] and col != i:
            return False
        if num == puzzle[i][col] and row != i:
            return False
        
    rowStart = row//3 * 3
    colStart = col//3 * 3
    
    for i in range(3):
        for j in range(3):
            if num == puzzle[rowStart+i][colStart+j] and (row != rowStart+i and col != colStart+j):
                return False

    return True

def printPuzzle(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if (j+1)%3 == 0 and j+1<9:
                print(puzzle[i][j], end='|')
            else:
                print(puzzle[i][j], end=' ')
                
        print('')
        if (i+1)%3 == 0 and i+1<9:
            print('-----+-----+-----')
    

def solvePuzzle(puzzle):

    newPuzzle = copy.deepcopy(puzzle)

    editableValues = generateEditableValues(puzzle)

    index = 0

    while index < len(editableValues):
        
        noValueFound = True
        
        for i in range(editableValues[index][0], 10):
            if isValidValue(i, editableValues[index][1], editableValues[index][2], newPuzzle) and i != 0:
                editableValues[index][0] = i
                newPuzzle[editableValues[index][1]][editableValues[index][2]] = i
                index += 1
                noValueFound = False
                break
                
        if noValueFound:
            
            editableValues[index][0] = 0
            newPuzzle[editableValues[index][1]][editableValues[index][2]] = 0

            editableValues[index-1][0] += 1
            newPuzzle[editableValues[index-1][1]][editableValues[index-1][2]] = 0
            
            index -= 1
            
    return newPuzzle

def isPuzzleComplete(puzzle):
    
    for i in range(9):
        for j in range(9):
            if not isValidValue(puzzle[i][j], i, j, puzzle):
                return False
            
    return True

# Console Solution -------------------------------------------------------------------

def Main():
    
    solveRandomSudokoPuzzle = stringToArray(getRandomStringPuzzle()) # Solve random sudoko puzzle
    solveThisSudokoPuzzle = stringToArray("020604030450100206600005100004003000095201380200500907510000603807352000000000058") # Solve desired sudoko Puzzle

    puzzleToSolve = solveRandomSudokoPuzzle
    #puzzleToSolve = solveThisSudokoPuzzle
    
    printPuzzle(puzzleToSolve)
    print(" ")
    puzzleSolved = solvePuzzle(puzzleToSolve)
    printPuzzle(puzzleSolved)
    print(" ")
    print(isPuzzleComplete(puzzleSolved))
    
Main()



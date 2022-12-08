## Percolation Assignment
## 


from modules import percolatability as p

    

# Defining a variable to keep the grid size
gridSize = None

## Main Program
gridSize = p.extractArguments()
    
# Checking the validity of the entered grid size
grid = p.checkGridSize(gridSize)

# The first element of the grid result set is the validity of the entered grid size
# Therefore its if grid[0] == True then that means a valid grid size has been given
if grid[0] :
    # Displaying a message to the user, that we are proceeding with the valid input
    print('You entered a valid grid size, hence proceeding...')
    
    ## Defining two variables to hold the number of rows and number of columns
    numberOfColumns = grid[1][1] # The grid[1] is a tuple with two elements and second of that is number of columns
    numberOfRows = grid[1][0] # first element of the tuple is the number of rows

    populatedGrid = p.populatingGrid(numberOfRows, numberOfColumns)
    
    # Now we need to check the validity of each column for percolation
    # Now we will have the information like below
    # Let's say we have three rows and 4 columns
    # [ 23, 56, 78, '  ' ]
    # [ '  ', 43, 87, 65 ]
    # [ 71, 39, 98, 52 ]
    # That's how the data is sitting inside the grid
    # This is a lists in a list case
    # the outer list is the represents the rows, the first elements of that will have the complete first row with all the columns for row 1
    # The second element represents the second row, and that list has all the elements for columns in the second row etc
    # We need to check the column wise data to check whether the column is percolatable or not
    # If the the complete colum is filled with two digit numbers then that column is not percolatable
    # Therefore we have to check whether complete column is filled with two digit numbers or not. 

    # Defining a variable to check the validity of the columns. 
    validColumns = list()
    
    validColumns = p.checkPercolatability(populatedGrid, numberOfRows, numberOfColumns)
    
    #print('Percolate Validity : ')
    #print(validColumns)

    p.printResult(populatedGrid,validColumns, numberOfRows, numberOfColumns)
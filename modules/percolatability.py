## Doing the Assignment with Python modules
## This module contains all the functions required for the project
def extractArguments():
    import sys # sys module is used to extract the command line arguments

    ## Checking if the proper grid size is given or not
    ## When getting the argument size from command line using the sys.argv we get the file name as first argument and argument value from 2nd onwards
    if len(sys.argv) != 2 :
        # If we don't have 2 arguments then that means a grid size was not specified. 
        print('You did not specify a grid size, therefore using the default 5 x 5 grid size')
        # Setting the default grid size 
        gridSize = '5x5' # default grid size is 5x5
    else:
        # Grid Size has been specified, we can get it from 2nd argument value as below
        userGridSize = sys.argv[1]
        ## Displaying the entered grid size
        #print(f'You entered {userGridSize} as the grid size')
        # Setting the gridsize to user entered grid size value
        gridSize = userGridSize

    # Returning the gridSize
    return gridSize

## Defining a function to check the validity of the entered grid size
def checkGridSize(gridSizeInput):
    # The min Row and Columne count = 3
    # The max Row and Column count = 9
    # There for the input for the gridsize has maximum 3 characters 
    # Example 3x4 9x9
    # Checking the lengh of the input the max length is 3 characters
    input_length = len(gridSizeInput)
    
    # Defining two variables to keep the row length and column length
    rows, columns = (0,0)

    # always the 2 character of the input should be a 'x'
    # converting the input string to lower case to convert X and x into x for easy validation 
    # also we shold only have one x character in the input string otherwise input is not a valid input example: xx5 Xx9 is not a valid input
    if gridSizeInput.lower()[1] == 'x' and gridSizeInput.lower().count('x') == 1 and input_length == 3:
        # using the string split function to split the row size and column size 
        rows, columns = gridSizeInput.lower().split('x')
        # Printing the extracted number of rows and columns
        #print(f'Rows {rows} and columns {columns}')0
    else:
        ## If above conditions are not met then the input is not valid
        print(f'{gridSizeInput} is not a valid grid size')
        # Defining a variable to validate the validity of the input string
        valid = False

    # Checking whether row / column sizes are integer
    try:
        # Addiontionally the row size and column sizes should be integer, therefore should be able to convert to integer
        rows, columns = int(rows), int(columns)

        # Also the min row / column size is 3 and max row / column size is 9, therefore checking for that condition
        if ( rows >= 3 and rows <= 9 ) and  ( columns >= 3 and columns <= 9 ):
            # values can be converted to integer as well as they are within the range, therefore input is valid
            valid = True
        else:
            # values can be converted to integer but they are out of range
            print('Not a valid grid size. They are out of range. Min Row / Column size is 3 and Max Row / Column Size is 9')
            valid = False

    except:
        # values can't be converted to integer therefore not a valid input
        print('Not a valid input grid size')
        valid = False

    # Returning the inputs back to the main program
    return (valid, (rows, columns))

## Defining a function to populated the Grid
def populatingGrid(numberOfRows,numberOfColumns):

    import random # random module is used to generate random integers
    
    # Defining a variable to keep the values of the row elementsh
    # We will take row by row and get populate the columns with randon integers
    gridRows = list()
    
    ## Iterating for all rows, one by one
    for i in range(numberOfRows):
        # Defining another list to keep the column values
        gridColums = list()

        #print(' Number of Columns : ', numberOfColumns)
        # Now for each row, we are going to iterate for number or columns and populate that with the random integers
        for j in range(numberOfColumns):
            # First we need to check whether we should populate the cell (column) with a two digit value of should we keep it empty
            # Therefore, first generating a random integer between 0 and 1 including them. 
            # If zero then the cell / column element should be empty if 1 we should populate it with a two digit number.
            emptryCellOrValue = random.randint(0,1)

            # if the value is 1 then the column should not be empty, we need to populate it with a two digit number
            if emptryCellOrValue == 1:
                # generating a random two digit number between 10, 99 and appending that to the column list 
                gridColums.append(random.randint(10,99))
            else:
                # if the value is 0 then we should keep the cell / column value as empty. therefore appending it with a '  ' (double spaces)
                # double spaces are using to match the two digits for better formating of the end result
                gridColums.append('  ')

        #print('New Column : ')
        #print(gridColums)
        
        # Adding the rull row with columns into the grid rows variable
        gridRows.append(gridColums)

    
    ## We have now finished generating the grid and populating it with the random integers
    print('Populated Grid successfully...')
    
    return gridRows

# Defining a function to check the percolatability
def checkPercolatability(gridRows, numberOfRows,numberOfColumns):
    # Defining variable to keep the valid columns
    validColumns = list() 
    
    ## Now we need to check all the columns and see whether we have two digit numbers in all rows of that column 
    ## picking each column and iterating over the rows thereafter  
    for column in range(numberOfColumns):
        #print(' Current column : ', column)
        # Defining another list to check whether each row element of the column had a two digit number or not
        valid = list()

        # picking a single column and iterating over all the rows
        for row in range(numberOfRows):
            #print('Current row : ', row)
            # Curreent value of the row element
            currentValue = gridRows[row][column]
            #print('Current Value = ', currentValue)

            # if the row element is not equal to a '  ' / double spaces, that means it has a two digit number
            if  currentValue != '  ':
                valid.append('Not Empty') 
            else:
                valid.append('Empty') 
        # Now we need to check whether all rows of that column had a two digit number or not
        # if all the rows had then the count of True should be equal to the number of rows
        # Defining a variable to hold the count of True elements in the valid list
        countOfEmpty = 0 

        # Iterating over the valid list to count the number of 
        for m in range(numberOfRows):
            if valid[m] == 'Empty':
                countOfEmpty += 1

        # if the count of empty rows is zero that means each row is filled with a two digit number
        # that means that column is not percolatable
        # if the complete column is empty that
        if countOfEmpty > 0 :
            validColumns.append('OK') 
        else:
            validColumns.append('NO')

    return validColumns

## Defining function to print the final results
def printResult(gridRows,validColumns,numberOfRows,numberOfColumns):
    # Now Printing the Final Result
    print('Final Result on Percolation ')

    # First printing the grid
    for a in range(numberOfRows):
        for b in range(numberOfColumns):
            print(gridRows[a][b], end= ' ')
        
        print('')

    # Now printing the percolatability of the column
    for c in range(numberOfColumns):
        print(validColumns[c], end= ' ')
        

    print(' ')
    print('Thank you!')
# How do you flip a matrix clockwise or counter-clockwise?

# Flipping clockwise
# Transpose the matrix, then reverse each row 

def rotate_clockwise(matrix):
    # assume the matrix is n x n 
    # if not, for an m x n matrix we construct a new n x m for transposing 
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(len(matrix)):
        l, r = 0, len(matrix[0])-1 
        while l < r:
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1

# Flipping counter clockwise 
# Reverse each row, then transpose the matrix 

def rotate_clockwise(matrix):    
    # assume the matrix is n x n 
    # if not, for an m x n matrix we construct a new n x m for transposing 
    for i in range(len(matrix)):
        l, r = 0, len(matrix[0])-1 
        while l < r:
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1

    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Flipping 180 degrees 
# Reverse each row, reverse each col

def rotate_flip(matrix):
    for i in range(len(matrix)):
        l, r = 0, len(matrix[0])-1 
        while l < r:
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1

    for j in range(len(matrix[0])):
        top, bot = 0, len(matrix)-1 
        while top < bot:
            matrix[top][j], matrix[bot][j] = matrix[bot][j], matrix[top][j]
            top += 1
            bot -= 1

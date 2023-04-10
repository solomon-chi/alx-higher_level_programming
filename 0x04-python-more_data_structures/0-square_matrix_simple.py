def square_matrix_simple(matrix):
    # Create new matrix with same dimensions as input matrix
    new_matrix = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
    
    # Iterate over each row
    for i in range(len(matrix)):
        # Iterate over each element of the row
        for j in range(len(matrix[i])):
            # Compute the square of the current element
            square = matrix[i][j] ** 2
            # Append the square to the current row of new_matrix
            new_matrix[i][j] = square
    
    # Return the new matrix
    return new_matrix


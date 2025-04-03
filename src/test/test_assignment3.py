#This file is the same thing as assignment3.py with the exception of this line.

import numpy as np

#Question 1
def gauss_elimination(a_matrix, b_matrix):
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("Error: A is not a square matrix")
        return
    if b_matrix.shape[1] > 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("Error: Check that b vector is entered correctly.")
        return


    n = len(b_matrix)
    m = n - 1
    i = 0
    j = i - 1
    x = np.zeros(n)
    new_line = "\n"

    #Create augmented matrix
    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis=1, dtype=float)

    while i<n:
        if augmented_matrix[i][i] == 0:
            print("Divide by 0 error")
            return

        for j in range(i+1, n):
            scaling_factor = augmented_matrix[j][i]/augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - (scaling_factor*augmented_matrix[i])
            #print(augmented_matrix)
        i = i+1

    #Backwards substitution
    x[m] = augmented_matrix[m][n] / augmented_matrix[m][m]

    for k in range(n-2, -1, -1):
        x[k] = augmented_matrix[k][n]

        for j in range(k+1, n):
            x[k] = x[k]/augmented_matrix[k][k]
    print(f"Question 1: {x}")
a1 = np.array([[2,-1,1], [1,3,1], [-1,5,4]])
b1 = np.array([[6], [0], [3]])
gauss_elimination(a1,b1)

#Question 2
def lu_decomposition(matrix):
    """
    Performs LU decomposition of a square matrix.

    Args:
        matrix: A square matrix (list of lists or numpy array).

    Returns:
        A tuple containing L (lower triangular matrix) and U (upper triangular matrix).
    """
    n = len(matrix)
    L = np.eye(n)
    U = np.array(matrix, dtype=float)

    for i in range(n):
        for k in range(i + 1, n):
            factor = U[k][i] / U[i][i]
            L[k][i] = factor
            U[k] = U[k] - factor * U[i]

    return L, U

# Example usage:
matrix_a = [[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]]
L, U = lu_decomposition(matrix_a)

print("Question 2:")
det = np.linalg.det(matrix_a)
print()
print(f"Determinant: {det}")
print("L:")
print(L)
print("U:")
print(U)

#Question 3
def is_diagonally_dominant(matrix):
    A = np.array(matrix)
    abs_A = np.abs(A)
    for i in range(len(A)):
        diag_val = abs_A[i, i]
        row_sum = np.sum(abs_A[i, :]) - diag_val
        if diag_val < row_sum:
            print("Not diagonally dominant.")
            break
    else:
        print("Diagonally dominant.")

matrix_3 = [[9, 0, 5, 2, 1], [3, 9, 1, 2, 1], [0, 1, 7, 2, 3], [4, 2, 3, 12, 2], [3, 2, 4, 0, 8]]
print("Question 3:")
is_diagonally_dominant(matrix_3)

#Question 4
def is_positive_definite(matrix):

    if not np.all(np.linalg.eigvals(matrix) > 0):
        print("Not positive definite.")
    else:
        print("Positive definite.")

matrix_4 = [[2, 2, 1], [2, 3, 0], [1, 0, 2]]
print("Question 4:")
is_positive_definite(matrix_4)

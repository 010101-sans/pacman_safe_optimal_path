import random

matrix = [[' ' for _ in range(8)] for _ in range(8)]

# Place 4 '*' at random row and column
for _ in range(4):
    row = random.randint(0, 7)
    col = random.randint(0, 7)
    matrix[row][col] = '*'

# Place 'P' at random row and column
row = random.randint(0, 7)
col = random.randint(0, 7)
matrix[row][col] = 'P'

# Print the matrix
for row in matrix:
    print(' '.join(row))

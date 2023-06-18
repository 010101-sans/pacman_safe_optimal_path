import random, os

matrix = None

def setup():
    global matrix
    
    matrix = [[' ' for _ in range(8)] for _ in range(8)]
    marked_places = set()

    # Place 4 '*' at random row and column
    for _ in range(4):
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        if (row, col) not in marked_places:
            matrix[row][col] = '*'
            marked_places.add((row, col))

    # Place 'P' at random row and column
    while True:
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        if (row,col) not in marked_places:
            matrix[row][col] = 'P'
            marked_places.add((row, col))
            break

# Print the matrix
def print_matrix():
    global matrix
    
    print("\n+", "---+" * 8, sep="", end="")
    for row in matrix:
        print("\n|", end="")
        for ele in row:
            print(f" {ele} |", end="")
    print("\n+", "---+" * 8, sep="")
    
os.system("cls")
setup()
print_matrix()
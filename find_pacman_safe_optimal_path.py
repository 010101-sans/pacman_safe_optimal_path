import pprint, os, heapq, time

def get_direction_symbol(prev_position, current_position):
    if current_position[0] < prev_position[0]:
        return '^'
    elif current_position[0] > prev_position[0]:
        return 'v'
    elif current_position[1] < prev_position[1]:
        return '<'
    elif current_position[1] > prev_position[1]:
        return '>'
    else:
        return 'P'

def print_path_in_grid(output_list):
    grid = [[' ' for _ in range(8)] for _ in range(8)]

    for i in range(len(output_list)):
        position = output_list[i]
        row, col = position
        prev_position = output_list[i-1] if i > 0 else position
        direction = get_direction_symbol(prev_position, position)
        grid[row][col] = direction

        print("\033[2J\033[H", end="")
        time.sleep(1/5)

        print("    0   1   2   3   4   5   6   7")
        print("  +---+---+---+---+---+---+---+---+")

        for i in range(8):
            print(f"{i} |", end=" ")
            for j in range(8):
                print(f"{grid[i][j]} |", end=" ")
            print("\n  +---+---+---+---+---+---+---+---+")
            
    time.sleep(2)

    

def dijkstra(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])

    distance = [[float('inf')] * cols for _ in range(rows)]
    distance[start[0]][start[1]] = 0

    heap = [(0, start)]
    heapq.heapify(heap)

    while heap:
        dist, current = heapq.heappop(heap)

        if current == end:
            return backtrack_path(grid, start, current)

        row, col = current
        neighbors = get_neighbors(grid, row, col)

        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor
            new_dist = dist + 1  # Each movement has a cost of 1

            if new_dist < distance[neighbor_row][neighbor_col]:
                distance[neighbor_row][neighbor_col] = new_dist
                heapq.heappush(heap, (new_dist, (neighbor_row, neighbor_col)))
                grid[neighbor_row][neighbor_col] = current

    return None

def backtrack_path(grid, start, end):
    path = []
    current = end

    while current != start:
        path.append(current)
        row, col = current
        current = grid[row][col]

    path.append(start)
    path.reverse()
    return path

def get_neighbors(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    neighbors = []
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != 'G':
            neighbors.append((new_row, new_col))

    return neighbors

grid = [[' ' for _ in range(8)] for _ in range(8)]
grid[7][3] = 'P'

grid[0][1] = 'F'
grid[1][2] = 'F'
grid[2][5] = 'F'
grid[4][4] = 'F'
grid[5][6] = 'F'
grid[6][1] = 'F'

grid[1][1] = 'G'
grid[3][2] = 'G'
grid[5][2] = 'G'
grid[5][4] = 'G'

start = (7, 3)
ends = [(0, 1), (1, 2), (2, 5), (4, 4), (5, 6), (6, 1)]

path = []
for i in range(len(ends)):
    temp_path = dijkstra(grid, start, ends[i])
    if temp_path:
        path += temp_path[:-1]  # Exclude the last position since it will be visited in the next iteration
        start = ends[i]  # Update the starting position for the next iteration

os.system("cls")
if path:
    path.append(ends[-1])  # Append the last 'F' position
    print_path_in_grid(path)
    print()
    pprint.pprint(path)
    print(f"\nPath Length : {len(path)-1}\n")
else:
    print("No valid path found.")



''' 

     0   1   2   3   4   5   6   7
   +---+---+---+---+---+---+---+---+
 0 |   | F |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+
 1 |   | G | F |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+
 2 |   |   |   |   |   | F |   |   |
   +---+---+---+---+---+---+---+---+
 3 |   |   | G |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+
 4 |   |   |   |   | F |   |   |   |
   +---+---+---+---+---+---+---+---+
 5 |   |   | G |   | G |   | F |   |
   +---+---+---+---+---+---+---+---+
 6 | F |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+
 7 |   |   |   | P |   |   |   |   |
   +---+---+---+---+---+---+---+---+


[(7, 3),
(6, 3),
(5, 3),
(4, 3),
(3, 3),
(2, 3),
(1, 3),
(0, 3),
(0, 2),
(0, 1),
(0, 2),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(2, 5),
(2, 4),
(3, 4),
(4, 4),
(4, 5),
(4, 6),
(5, 6),
(5, 5),
(6, 5),
(6, 4),
(6, 3),
(6, 2),
(6, 1)]


    The time complexity of the code can be analyzed based on the major operations and loops
    present in the code :

    >>> Constructing the grid: 
        - This operation takes constant time as the grid size is fixed (8x8).

    >>> Dijkstra's algorithm:

        >>> Initializing distance matrix: 
            - This operation takes O(rows * cols) time, where rows and cols are the dimensions of the grid.

        >>> Initializing heap: 
            - This operation takes O(log V) time, where V is the number of vertices (cells) in the grid.

        >>> Main loop: 
        
            - The loop runs until the heap is empty, which can take a maximum of V iterations. 
        
            - Within each iteration:
                - Extracting the minimum distance node from the heap takes O(log V) time.
                - Finding neighbors of a node takes constant time since there are only four possible neighbors.
                - Updating the distance and pushing nodes to the heap take O(log V) time.
        
            Therefore, the overall time complexity of Dijkstra's algorithm :
                O((rows * cols) + V * (log V + log V)) = O(V * log V).

    >>> Backtracking the path: 
        - This operation takes O(V) time, as it traverses the path from the end to the start.

    >>> Printing the grid: 
        - Constructing the grid for printing takes constant time
        - Printing each element takes constant time. 
        - Therefore, the time complexity of grid printing is also constant.

    >>> Overall, the dominant factor in terms of time complexity is Dijkstra's algorithm, 
        which has a time complexity of O(V * log V).

'''
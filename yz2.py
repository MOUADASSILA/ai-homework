import math

# Maze 1
maze1 = [
    "#####B#",
    "##### #",
    "####  #",
    "#### ##",
    "     ##",
    "A######"
]

start1 = (5, 0)  # A's position
goal1 = (0, 5)   # B's position

# Maze 2
maze2 = [
    "###                 #########",
    "#   ###################   # #",
    "# ####                # # # #",
    "# ################### # # # #",
    "#                     # # # #",
    "##################### # # # #",
    "#   ##                # # # #",
    "# # ## ### ## ######### # # #",
    "# #    #   ##B#         # # #",
    "# # ## ################ # # #",
    "### ##             #### # # #",
    "### ############## ## # # # #",
    "###             ##    # # # #",
    "###### ######## ####### # # #",
    "###### ####             #   #",
    "A      ######################"
]

start2 = (14, 0)  # A's position
goal2 = (8, 15)   # B's position

# Maze 3
maze3 = [
    "##   #",
    "## ## #",
    "#B #  #",
    "# ## ##",
    "     ##",
    "A######"
]

start3 = (5, 0)  # A's position
goal3 = (2, 1)   # B's position

# Maze 4
maze4 = [
    "#######",
    "# #   #",
    "###B# #",
    "#     #",
    "# ## ##",
    "#     #",
    "# # #A#",
    "#     #",
    "#######"
]

start4 = (6, 6)  # A's position
goal4 = (2, 3)   # B's position

# Common functions for distance metrics
def cosine_similarity(v1, v2):
    dot_product = sum(x * y for x, y in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(x**2 for x in v1))
    magnitude_v2 = math.sqrt(sum(x**2 for x in v2))
    return dot_product / (magnitude_v1 * magnitude_v2)

def square_root_sum_of_squares(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def manhattan_distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def minkowski_distance(p1, p2, r):
    return (abs(p2[0] - p1[0])**r + abs(p2[1] - p1[1])**r)**(1/r)

# Functions for processing mazes
def process_maze(maze):
    maze = [list(row) for row in maze]
    height, width = len(maze), len(maze[0])
    positions = {'A': None, 'B': None}
    for i in range(height):
        for j in range(width):
            if maze[i][j] == 'A':
                positions['A'] = (i, j)
            elif maze[i][j] == 'B':
                positions['B'] = (i, j)
    return maze, positions

# Process mazes and calculate distances
maze1, positions1 = process_maze(maze1)
maze2, positions2 = process_maze(maze2)
maze3, positions3 = process_maze(maze3)
maze4, positions4 = process_maze(maze4)

# Calculate distances
cosine_dist1 = cosine_similarity(positions1['A'], positions1['B'])
sqrt_sum_of_squares_dist1 = square_root_sum_of_squares(positions1['A'], positions1['B'])
euclidean_dist1 = euclidean_distance(positions1['A'], positions1['B'])
manhattan_dist1 = manhattan_distance(positions1['A'], positions1['B'])
minkowski_dist1 = minkowski_distance(positions1['A'], positions1['B'], 3)

cosine_dist2 = cosine_similarity(positions2['A'], positions2['B'])
sqrt_sum_of_squares_dist2 = square_root_sum_of_squares(positions2['A'], positions2['B'])
euclidean_dist2 = euclidean_distance(positions2['A'], positions2['B'])
manhattan_dist2 = manhattan_distance(positions2['A'], positions2['B'])
minkowski_dist2 = minkowski_distance(positions2['A'], positions2['B'], 3)

cosine_dist3 = cosine_similarity(positions3['A'], positions3['B'])
sqrt_sum_of_squares_dist3 = square_root_sum_of_squares(positions3['A'], positions3['B'])
euclidean_dist3 = euclidean_distance(positions3['A'], positions3['B'])
manhattan_dist3 = manhattan_distance(positions3['A'], positions3['B'])
minkowski_dist3 = minkowski_distance(positions3['A'], positions3['B'], 2)

cosine_dist4 = cosine_similarity(positions4['A'], positions4['B'])
sqrt_sum_of_squares_dist4 = square_root_sum_of_squares(positions4['A'], positions4['B'])
euclidean_dist4 = euclidean_distance(positions4['A'], positions4['B'])
manhattan_dist4 = manhattan_distance(positions4['A'], positions4['B'])
minkowski_dist4 = minkowski_distance(positions4['A'], positions4['B'], 3)

# Print results
print(f"Maze 1:")
print(f"Cosine Similarity: {cosine_dist1}")
print(f"Square Root of Sum of Squares: {sqrt_sum_of_squares_dist1}")
print(f"Euclidean Distance: {euclidean_dist1}")
print(f"Manhattan Distance: {manhattan_dist1}")
print(f"Minkowski Distance (r=3): {minkowski_dist1}\n")

print(f"Maze 2:")
print(f"Cosine Similarity: {cosine_dist2}")
print(f"Square Root Distance: {sqrt_sum_of_squares_dist2}")
print(f"Euclidean Distance: {euclidean_dist2}")
print(f"Manhattan Distance: {manhattan_dist2}")
print(f"Minkowski Distance (q=3): {minkowski_dist2}\n")

print(f"Maze 3:")
print(f"Cosine Similarity: {cosine_dist3}")
print(f"Square Root Distance: {sqrt_sum_of_squares_dist3}")
print(f"Euclidean Distance: {euclidean_dist3}")
print(f"Manhattan Distance: {manhattan_dist3}")
print(f"Minkowski Distance (p=2): {minkowski_dist3}\n")

print(f"Maze 4:")
print(f"Cosine Similarity: {cosine_dist4}")
print(f"Square Root Distance: {sqrt_sum_of_squares_dist4}")
print(f"Euclidean Distance: {euclidean_dist4}")
print(f"Manhattan Distance: {manhattan_dist4}")
print(f"Minkowski Distance (p=3): {minkowski_dist4}")

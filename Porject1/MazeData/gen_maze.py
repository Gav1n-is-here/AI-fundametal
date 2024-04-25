import random

def generate_maze(n, m):
    maze = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]
    maze[0][0] = 0  # Starting point
    maze[n - 1][m - 1] = 0  # Ending point

    while not has_path(maze, n, m):
        maze = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]
        maze[0][0] = 0  # Starting point
        maze[n - 1][m - 1] = 0  # Ending point

    return maze

def has_path(maze, n, m):
    visited = set()
    stack = [(0, 0)]

    while stack:
        x, y = stack.pop()
        if (x, y) == (n - 1, m - 1):
            return True
        visited.add((x, y))

        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for nx, ny in neighbors:
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))

    return False

def write_maze_to_file(maze, file_name):
    with open(file_name, 'a') as file:
        file.write(f"{len(maze)} {len(maze[0])}\n")
        for row in maze:
            file.write(' '.join(map(str, row)) + '\n')

# Generate and write maze to file
n, m = 10, 10  # Adjust dimensions as needed


input_str = input("输入规模，输入 0 使用默认")

if len(input_str.split()) == 2:
    a, b = map(int, input_str.split())
    n, m = a, b
    print(f"生成规模{n}x{m} ")
elif input_str.strip() == '0':
    n, m = 10, 10
    print("默认规模10x10")
else:
    print("ERROR")

maze = generate_maze(n, m)
write_maze_to_file(maze, 'maze.txt')

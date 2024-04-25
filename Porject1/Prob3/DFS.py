def valid(matrix, visited, x, y):
    n, m = len(matrix), len(matrix[0])
    return 0 <= x < n and 0 <= y < m and matrix[x][y] == 0 and not visited[x][y]

def dfs(matrix, visited, path, x, y, dest_x, dest_y):
    global maze
    
    if x == dest_x and y == dest_y:
        path.append((x, y))
        return True
    if valid(matrix, visited, x, y):
        maze[x][y]=2
        visited[x][y] = True
        path.append((x, y))
        if (dfs(matrix, visited, path, x + 1, y, dest_x, dest_y) or
                dfs(matrix, visited, path, x, y + 1, dest_x, dest_y) or
                dfs(matrix, visited, path, x - 1, y, dest_x, dest_y) or
                dfs(matrix, visited, path, x, y - 1, dest_x, dest_y)):
            return True
        path.pop()
        visited[x][y] = False
    return False

def find_path_dfs(matrix):
    global maze
    n, m = len(matrix), len(matrix[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    path = []
    if dfs(matrix, visited, path, 0, 0, n - 1, m - 1):
        # for i in range(n):
        #     for j in range(m):
        #         if visited[i][j]:
        #             matrix[i][j] = 2
        return path
    else:
        return None
    


import matplotlib.pyplot as plt

def visualize_maze_with_path(maze, path):
    plt.figure(figsize=(len(maze[0]), len(maze)))  # 设置图形大小
    plt.imshow(maze, cmap='Greys', interpolation='nearest')  # 使用灰度色图，并关闭插值

    # 绘制路径
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker='o', markersize=8, color='red', linewidth=3)

    # 染色值为2的位置为浅蓝色
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                plt.fill([j-0.5, j+0.5, j+0.5, j-0.5], [i-0.5, i-0.5, i+0.5, i+0.5], color='lightblue')

    # 设置坐标轴刻度和边框
    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)

    plt.axis('on')  # 显示坐标轴
    plt.show()




n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
global maze
maze = [[0 for _ in range(m)] for _ in range(n)]

path = find_path_dfs(matrix)

if path:
    # print(path)
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                    maze[i][j] = 4

    maze[n-1][m-1]=2
    visualize_maze_with_path(maze, path)
else:
    print("No path found.")


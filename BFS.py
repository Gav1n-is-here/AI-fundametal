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

from collections import deque

def valid(matrix, visited, x, y):
    n, m = len(matrix), len(matrix[0])
    return 0 <= x < n and 0 <= y < m and matrix[x][y] == 0 and not visited[x][y]


def bfs(matrix, visited, start_x, start_y, dest_x, dest_y):
    queue = deque([(start_x, start_y, [])])
    visited[start_x][start_y] = True

    while queue:
        x, y, path = queue.popleft()
        path = path + [(x, y)]

        if x == dest_x and y == dest_y:
            return path

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if valid(matrix, visited, nx, ny):
                queue.append((nx, ny, path[:]))
                visited[nx][ny] = True

    return None  

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

global maze
maze = [[0 for _ in range(m)] for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
path_bfs = bfs(matrix, visited, 0, 0, n - 1, m - 1)

if path_bfs:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                maze[i][j] = 4
            if visited[i][j]==True:
                maze[i][j] = 2

    maze[n - 1][m - 1] = 2
    print(maze)
    visualize_maze_with_path(maze, path_bfs)
else:
    print("No path found.")


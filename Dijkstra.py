import heapq

class Node:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance
        self.parent = None 

    def __lt__(self, other):
        return self.distance < other.distance

def dijkstra(matrix, start_x, start_y, dest_x, dest_y):
    n, m = len(matrix), len(matrix[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    min_heap = []
    heapq.heappush(min_heap, Node(start_x, start_y, 0))

    while min_heap:
        curr = heapq.heappop(min_heap)
        x, y, distance = curr.x, curr.y, curr.distance

        if x == dest_x and y == dest_y:
            path = []
            while curr:
                path.append((curr.x, curr.y))
                visited[curr.x][curr.y] = True 
                curr = curr.parent
            path.reverse()
            return path, visited

        if not visited[x][y]:
            visited[x][y] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0 and not visited[nx][ny]:
                    new_distance = distance + 1  
                    heapq.heappush(min_heap, Node(nx, ny, new_distance))
                    min_heap[-1].parent = curr  

    return None, visited 

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
maze = [[0 for _ in range(m)] for _ in range(n)]


path_dijkstra, visited_nodes_dijkstra = dijkstra(matrix, 0, 0, n-1, m-1)
if path_dijkstra:
    # print("Dijkstra Algorithm Path:", path_dijkstra)
    # print("Visited Nodes Matrix:", visited_nodes_dijkstra)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                maze[i][j] = 4
            if visited_nodes_dijkstra[i][j]==True:
                maze[i][j] = 2

    maze[n - 1][m - 1] = 2
    # print(maze)
    visualize_maze_with_path(maze,path_dijkstra)
else:
    print("No path found.")


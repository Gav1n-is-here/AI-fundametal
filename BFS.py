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














# char=input().split(' ')
# n=int(char[0])
# m=int(char[1])
# matrix = [[0 for _ in range(m)] for _ in range(n)]
# for _ in range(0,n):
#     char=input().split(' ')
#     for i in range(0,m):
#         matrix[_][i]=char[i]
# # print(matrix)





# from collections import deque
# import heapq

# # 迷宫问题的节点类
# class Node:
#     def __init__(self, x, y, parent=None):
#         self.x = x
#         self.y = y
#         self.parent = parent
#         self.cost = 0

#     def __lt__(self, other):
#         return self.cost < other.cost



# # 定义迷宫，0表示可通行，1表示障碍物
# # maze = [
# #     [0, 1, 0, 0, 0],
# #     [0, 1, 0, 1, 0],
# #     [0, 0, 0, 0, 0],
# #     [0, 1, 1, 1, 0],
# #     [0, 0, 0, 1, 0]
# # ]

# maze=matrix
# # 方向数组，用于表示上、下、左、右四个方向的移动
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 判断当前位置是否合法
# def is_valid(x, y):
#     return 0 <= x < n and 0 <= y < m and maze[x][y] == 0

# # 深度优先搜索（DFS）
# def dfs(x, y):
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     stack = [(x, y)]
#     path = []
#     while stack:
#         cur_x, cur_y = stack.pop()
#         path.append((cur_x, cur_y))
#         if cur_x == n - 1 and cur_y == m - 1:
#             return path
#         visited[cur_x][cur_y] = True
#         for i in range(4):
#             new_x, new_y = cur_x + dx[i], cur_y + dy[i]
#             if is_valid(new_x, new_y) and not visited[new_x][new_y]:
#                 stack.append((new_x, new_y))
#     return []

# # 广度优先搜索（BFS）
# def bfs(x, y):
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     queue = deque([(x, y)])
#     path = []
#     while queue:
#         cur_x, cur_y = queue.popleft()
#         path.append((cur_x, cur_y))
#         if cur_x == n - 1 and cur_y == m - 1:
#             return path
#         visited[cur_x][cur_y] = True
#         for i in range(4):
#             new_x, new_y = cur_x + dx[i], cur_y + dy[i]
#             if is_valid(new_x, new_y) and not visited[new_x][new_y]:
#                 queue.append((new_x, new_y))
#     return []

# # 迪杰斯特拉算法
# def dijkstra(x, y):
#     pq = [(0, Node(x, y))]
#     heapq.heapify(pq)
#     dist = {node: float('inf') for node in pq}
#     dist[pq[0][1]] = 0
#     path = []
#     while pq:
#         cost, node = heapq.heappop(pq)
#         path.append((node.x, node.y))
#         if node.x == n - 1 and node.y == m - 1:
#             return path
#         if cost > dist[node]:
#             continue
#         for i in range(4):
#             new_x, new_y = node.x + dx[i], node.y + dy[i]
#             if is_valid(new_x, new_y):
#                 new_cost = node.cost + 1
#                 if new_cost < dist[Node(new_x, new_y)]:
#                     dist[Node(new_x, new_y)] = new_cost
#                     heapq.heappush(pq, (new_cost, Node(new_x, new_y, node)))
#     return []

# # A*算法
# def heuristic(node):
#     return abs(node.x - (n - 1)) + abs(node.y - (m - 1))

# def astar(x, y):
#     pq = [(heuristic(Node(x, y)), Node(x, y))]
#     heapq.heapify(pq)
#     dist = {node: float('inf') for node in pq}
#     dist[pq[0][1]] = 0
#     path = []
#     while pq:
#         cost, node = heapq.heappop(pq)
#         path.append((node.x, node.y))
#         if node.x == n - 1 and node.y == m - 1:
#             return path
#         if cost > dist[node]:
#             continue
#         for i in range(4):
#             new_x, new_y = node.x + dx[i], node.y + dy[i]
#             if is_valid(new_x, new_y):
#                 new_cost = node.cost + 1
#                 if new_cost < dist[Node(new_x, new_y)]:
#                     dist[Node(new_x, new_y)] = new_cost
#                     heapq.heappush(pq, (new_cost + heuristic(Node(new_x, new_y)), Node(new_x, new_y, node)))
#     return []

# # 测试
# print("DFS:", dfs(0, 0))
# print("BFS:", bfs(0, 0))
# print("Dijkstra:", dijkstra(0, 0))
# print("A*:", astar(0, 0))
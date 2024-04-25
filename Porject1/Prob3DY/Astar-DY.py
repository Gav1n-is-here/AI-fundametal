heuristic_mode='曼哈顿距离' # 129 # 90
#heuristic_mode='对角线距离' #194 # 188
#heuristic_mode='切比雪夫距离' #181 #189
import heapq
import math
class Node:
    def __init__(self, x, y, g_cost, h_cost):
        self.x = x
        self.y = y
        self.g_cost = g_cost 
        self.h_cost = h_cost 
        self.f_cost = g_cost + h_cost  
        self.parent = None 

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def heuristic(node, dest_x, dest_y):
    if heuristic_mode=='曼哈顿距离':
        return abs(node.x - dest_x) + abs(node.y - dest_y) 
    elif heuristic_mode=='对角线距离':
        dx = abs(node.x - dest_x)
        dy = abs(node.y - dest_y)
        return max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)
    elif heuristic_mode=='切比雪夫距离':
        return max(abs(node.x - dest_x), abs(node.y - dest_y))
import tkinter as tk
from tkinter import messagebox
def show_message(len_visited,len_path):
    if heuristic_mode=='曼哈顿距离':
        message = f"使用曼哈顿距离,搜索了: {len_visited}, 路长: {len_path}"
        messagebox.showinfo("A*", message)
    elif heuristic_mode=='对角线距离':
        message = f"对角线距离,搜索了: {len_visited}, 路长: {len_path}"
        messagebox.showinfo("A*", message)
    elif heuristic_mode=='切比雪夫距离':
        message = f"切比雪夫距离,搜索了: {len_visited}, 路长: {len_path}"
        messagebox.showinfo("A*", message)


def a_star(matrix, start_x, start_y, dest_x, dest_y):
    n, m = len(matrix), len(matrix[0])
    visited = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    min_heap = []
    heapq.heappush(min_heap, Node(start_x, start_y, 0, heuristic(Node(start_x, start_y, 0, 0), dest_x, dest_y)))

    while min_heap:
        curr = heapq.heappop(min_heap)
        x, y = curr.x, curr.y

        if x == dest_x and y == dest_y:
            path = []
            while curr:
                path.append((curr.x, curr.y))
                visited.append((curr.x,curr.y ))
                curr = curr.parent
            path.reverse()
            return path, visited
        visited.append((x,y ))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0 and (nx,ny) not in visited:
                new_node = Node(nx, ny, curr.g_cost + 1, heuristic(Node(nx, ny, 0, 0), dest_x, dest_y))
                new_node.parent = curr  
                heapq.heappush(min_heap, new_node)

    return None, visited  

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
def visualize_Astar_animation(maze,path, visited_list):
    fig, ax = plt.subplots()
    ax.imshow(maze, cmap='Greys', interpolation='nearest')

    def update(frame):
        if frame < len(visited_list):
            row, col = visited_list[frame]
            # ax.imshow(maze, cmap='Greys', interpolation='nearest')  #这一行影响了性能！！！
            ax.add_patch(Rectangle((col-0.5, row-0.5), 1, 1, color='grey'))
        else :
            prey=-1
            prex=-1
            for _ in path:
                ax.plot( _[1], _[0], marker='o', markersize=8, color='yellow', linewidth=3)
                if prey==-1 and prex==-1:
                    prey=_[1]
                    prex=_[0]
                else:
                    ax.plot([prey, _[1]], [prex, _[0]], color='yellow')
                    prey=_[1]
                    prex=_[0]
    ani = FuncAnimation(fig, update, frames=len(visited_list)+1, repeat=False, interval=30)  
    plt.xticks()
    plt.yticks()
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)
    plt.axis('on')
    plt.title(f"Astar")
    plt.show()
    show_message(len(visited_list),len(path))


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

path_a_star, visited = a_star(matrix, 0, 0, n-1, m-1)
if path_a_star:
    visualize_Astar_animation(matrix,path_a_star, visited)

else:
    print("No path found.")
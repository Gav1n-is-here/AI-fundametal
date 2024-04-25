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
    visited = []
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
                visited.append((curr.x,curr.y ))
                curr = curr.parent
            path.reverse()
            return path, visited

        if  (x,y) not in visited:
            visited.append((x,y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0 and (nx,ny) not in visited:
                    new_distance = distance + 1  
                    heapq.heappush(min_heap, Node(nx, ny, new_distance))
                    min_heap[-1].parent = curr  

    return None, visited 

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
def visualize_Dijkstra_animation(maze,path, visited_list):
    fig, ax = plt.subplots()
    ax.imshow(maze, cmap='Greys', interpolation='nearest')

    def update(frame):
        if frame < len(visited_list):
            row, col = visited_list[frame]
            # ax.imshow(maze, cmap='Greys', interpolation='nearest')  
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

    # plt.xticks(range(len(maze[0])))
    # plt.yticks(range(len(maze)))
    plt.xticks()
    plt.yticks()
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)
    plt.axis('on')
    plt.title(f"Dijkstra")
    plt.show()



n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


path_dijkstra, visited_nodes_dijkstra = dijkstra(matrix, 0, 0, n-1, m-1)
if path_dijkstra:
    visualize_Dijkstra_animation(matrix,path_dijkstra, visited_nodes_dijkstra)
else:
    print("No path found.")


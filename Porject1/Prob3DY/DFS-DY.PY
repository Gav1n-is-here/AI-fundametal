import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
def visualize_dfs_animation(maze,path, visited_list):
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
    plt.title(f"Dfs")
    plt.show()

def valid(matrix, visited, x, y):
    n, m = len(matrix), len(matrix[0])
    if (x, y)  in visited:
        return 0
    return 0 <= x < n and 0 <= y < m and matrix[x][y] == 0 

def dfs(matrix, visited, path, x, y, dest_x, dest_y):
    if x == dest_x and y == dest_y:
        path.append((x, y))
        visited.append((x, y))
        return True
    if valid(matrix, visited, x, y):
        path.append((x, y))
        visited.append((x, y))
        if (dfs(matrix, visited, path, x + 1, y, dest_x, dest_y) or
                dfs(matrix, visited, path, x, y + 1, dest_x, dest_y) or
                dfs(matrix, visited, path, x - 1, y, dest_x, dest_y) or
                dfs(matrix, visited, path, x, y - 1, dest_x, dest_y)):
            return True
        path.pop()
        
    return False

def find_path_dfs(matrix):
    n, m = len(matrix), len(matrix[0])
    visited=[]
    path = []
    if dfs(matrix, visited, path, 0, 0, n - 1, m - 1):
        visualize_dfs_animation(matrix, path,visited)
        return path
    else:
        return None

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
path = find_path_dfs(matrix)


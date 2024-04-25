import random

def generate_maze(n, m):
    maze = [[random.randint(0, 5) for _ in range(m)] for _ in range(n)]
    return maze

def write_maze_to_file(maze, filename):
    with open(filename, 'a') as file:
        file.write(f"{len(maze)} {len(maze[0])}\n")
        for row in maze:
            file.write(' '.join(map(str, row)) + '\n')

# 生成迷宫


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

# 写入文件
filename = 'maze_moreval.txt'
write_maze_to_file(maze, filename)

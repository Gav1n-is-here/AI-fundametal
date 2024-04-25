#BFS
import  sys   

sys.setrecursionlimit(100000)
goal=['1','2','3','4','5','6','7','8','x']
start=input().split(' ')

def issolution(array):
    num = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] == 'x' or array[j] == 'x':
                continue
            if array[i] < array[j]:
                num += 1
    return num%2
if(issolution(start)):
    print(-1)


checked=[]
tree=[]
import copy
def move(char,index,order):
    re=copy.deepcopy(char)
    if order=='up':
        re[index]=re[index-3]
        re[index-3]='x'
        return re
    elif order=='down':
        re[index]=re[index+3]
        re[index+3]='x'
        return re
    elif order=='left':
        re[index]=re[index-1]
        re[index-1]='x'
        return re
    elif order=='right':
        re[index]=re[index+1]
        re[index+1]='x'
        return re


# tree.append(start)
# i=0

# while 1:
            # tmp=tree[1]

            # if tmp.index('x')<6:
            #     new=move(tmp,tmp.index('x'),'down')
            #     tree.append(new)
            #     continue
            # if tmp.index('x')%3!=0:
            #     new=move(tmp,tmp.index('x'),'left')
            #     tree.append(new)
            #     continue
            # if tmp.index('x')%3!=2:
            #     new=move(tmp,tmp.index('x'),'right')
            #     tree.append(new)
            #     continue
            # if tmp.index('x')>2:
            #     new=move(tmp,tmp.index('x'),'up')
            #     tree.append(new)
            #     continue
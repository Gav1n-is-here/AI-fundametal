#DFS
import  sys   
sys.setrecursionlimit(100000)
goal=['1','2','3','4','5','6','7','8','x']
start=input().split(' ')
x_index=start.index('x')
checked=[]

import copy
def move(char,index,order):
    re=copy.deepcopy(char)
    if order=='up':
        # re[index]=re[index-3]
        # re[index-3]='x'
        re[index],re[index-3]=re[index-3],'x'
        return re
    elif order=='down':
        # re[index]=re[index+3]
        # re[index+3]='x'
        re[index],re[index+3]=re[index+3],'x'
        return re
    elif order=='left':
        # re[index]=re[index-1]
        # re[index-1]='x'
        re[index],re[index-1]=re[index-1],'x'
        return re
    elif order=='right':
        # re[index]=re[index+1]
        # re[index+1]='x'
        re[index],re[index+1]=re[index+1],'x'
        return re
    
def dfs(char,index):
    global checked
    if char==goal:
          print(1)
          exit(0)
    if char in checked:
        return 0
    else:
        checked.append(char)
    tmp=char
    if index<6:
        new=move(tmp,index,'down')
        dfs(new,index+3)       
    if index%3!=0:
        new=move(tmp,index,'left')
        dfs(new,index-1)
    if index%3!=2:
        new=move(tmp,index,'right')
        dfs(new,index+1)
    if index>2:
        new=move(tmp,index,'up')
        dfs(new,index-3)
    return 0            
    

if dfs(start,x_index)==0:
    print(0)




    



# graph=[]
# for i in range(3):
#     list=[char[3*i],char[3*i+1],char[3*i+2]]
#     graph.append(list)
# print(graph)

#BFS最短路
char=input().split(' ')
n=int(char[0])
m=int(char[1])
graph=[]
for _ in range(n+1):
    graph.append([])
for _ in range(0,m):
    char=input().split(' ')
    a=int(char[0])
    b=int(char[1]) 
    if(a==b):
        continue
    else:
        graph[a].append(b)
pre={}
for _ in range(n+1):
    graph[_]=list(set(graph[_]))
    pre[_]=0

def BFS(graph,node):
    queue=[]
    seen=set()
    queue.append(node) 
    seen.add(node)
    
    while (len(queue)>0) :       
        ver =  queue.pop(0)        
        notes = graph[ver]       
        for i in notes:            
            if i not in seen:      
                queue.append(i)    
                seen.add(i)        
                pre[i]=ver
    return pre


pre=BFS(graph,1)
_ = n
length=-1
while _ != 0:
    length+=1
    _= pre[_]
print(length)
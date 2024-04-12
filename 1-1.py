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
    graph[_]=list(set(graph[_]))#去重
    pre[_]=0#前置节点dict

def BFS(graph,node):
    queue=[]
    seen=set()
    queue.append(node) 
    seen.add(node)
    
    while (len(queue)>0) :         #当队列里还有东西时
        ver =  queue.pop(0)        #取出队头元素
        notes = graph[ver]         #查看grep里面的key,对应的邻接点
        for i in notes:            #遍历邻接点
            if i not in seen:      #如果该邻接点还没出现过
                queue.append(i)    #存入queue
                seen.add(i)        #存入集合
                pre[i]=ver
    return pre


pre=BFS(graph,1)
_ = n
length=-1
while _ != 0:
    length+=1
    _= pre[_]
print(length)
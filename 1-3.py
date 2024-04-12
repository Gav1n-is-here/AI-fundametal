#堆优化版Dijkstra
from queue import PriorityQueue as PQ
pq=PQ()
char=input().split(' ')
n=int(char[0])
m=int(char[1])
graph=[]
dist=[]     #到i的最短距离
st=[]       #最短距离已经确定的集合
graph=[[0 for i in range(n)] for j in range(n)]
for _ in range(n):
    dist.append(10000)
    st.append(-1)
for _ in range(0,m):
    char=input().split(' ')
    x=int(char[0])
    y=int(char[1])
    z=int(char[2])
    if(x==y):
        continue
    else:
        graph[x-1][y-1]=z
# print(graph)
        

pq.put((0,0))
dist[0]=0
while(not pq.empty()):
    t=(pq.get())
    if(st[t[1]]==1):
        continue
    else:
        st[t[1]]=1
    
    for k in range(0,n):
        if(dist[k]>dist[t[1]] + graph[t[1]][k]):
            dist[k]=dist[t[1]] + graph[t[1]][k]
            pq.put((dist[k],k))
    if(st[n-1]==1):
        print(dist[n-1])

if(st[n-1]==-1):
        print(-1)


#朴素版Dijkstra
char=input().split(' ')
n=int(char[0])
m=int(char[1])
graph=[]
dist=[]     
st=[]       #已确定
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
st[0]=1
for _ in range(0,n):
    dist[_]=graph[0][_]
# print(dist)
for _ in range(1,n):
    t = -1
    for k in range(0,n):
        if (st[k]!=1 and (dist[k] < dist[t] or t == -1)):
            t = k
    st[t]=1
    for k in range(0,n):
        dist[k] = min(dist[k], dist[t] + graph[t][k])
    if(st[n-1]==1):
        print(dist[n-1])
if(st[n-1]==-1):
        print(-1)

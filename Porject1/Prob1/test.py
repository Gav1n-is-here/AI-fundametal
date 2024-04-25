from queue import PriorityQueue as PQ
pq=PQ()
pq.put((0,1))
print(pq.empty())
while(not pq.empty()):
    t=pq.get()
    print(t[1])

# 3 3
# 1 2 2
# 2 3 1
# 1 3 4
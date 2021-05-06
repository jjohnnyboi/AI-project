from queue import PriorityQueue

def greedybfs(graph, vert, goal):
    q = PriorityQueue()
    searchList = [vert.name]
    vert.visited = True
    cost = 0;
    # Add neighbours of start vertex to queue
    for i in vert.neighbors:
        q.put(i)
        searchList.append(i)
        cost += vert.neighbors[i]
        while q.empty() == False:
            u = q.get()
            if u == goal:
                break
            node_u = graph.vertices[u]
            node_u.visited = True

            for i in node_u.neighbors:
                node_v = graph.vertices[i]
                if node_v.visited == False and i not in searchList:
                    cost += node_u.neighbors[i]
                    q.put(i)
                    searchList.append(i)
        return searchList, cost

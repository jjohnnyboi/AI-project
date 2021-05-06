
def breadthSearch(graph, vert, goal):
    q = list()
    searchList = [vert.name]
    vert.visited = True
    cost = 0;
    returned = list()
    q.append((vert.name,0))
    # Add neighbours of start vertex to queue

    while len(q) > 0:
        u, cost = q.pop(0)
        if u == goal:
            returned.append(u)
            break
        node_u = graph.vertices[u]
        returned.append(node_u.name)
        node_u.visited = True

        for i in node_u.neighbors:
            node_v = graph.vertices[i]
            if node_v.visited == False and i not in searchList:
                ncost = cost + node_u.neighbors[node_v.name]
                q.append((i, ncost))
                searchList.append(i)

    return returned, cost

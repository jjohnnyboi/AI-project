def depthSearch(graph, start, goal):
    q = list()
    searchList = [start.name]
    start.visited = True
    # Add neighbours of start vertex to queue
    q.append((start.name,0))
    cost = 0;
    returned = list()
    while len(q) > 0:

        u, cost = q.pop()
        if u == goal:
            returned.append(u)
            break

        node_u = graph.vertices[u]
        node_u.visited = True
        returned.append(node_u.name)

        for i in node_u.neighbors:
            node_v = graph.vertices[i]

            if node_v.visited == False and i not in searchList:
                ncost = cost + node_u.neighbors[i]
                q.append((i, ncost))
                searchList.append(i)
    return returned, cost
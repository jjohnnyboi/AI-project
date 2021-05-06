def depthSearch(graph, start, goal):
    stack = list()
    searchList = [start.name]
    start.visited = True
    # Add neighbours of start vertex to queue
    stack.append(start.name)
    cost = 0;

    while (len(stack)):

        s = stack.pop()
        if s == goal:
            break

        node_u = graph.vertices[s]
        node_u.visited = True


        for i in node_u.neighbors:
            node_v = graph.vertices[i]

            if node_v.visited == False and i not in searchList:
                cost += node_u.neighbors[i]
                stack.append(i)
                searchList.append(i)
    return searchList, cost
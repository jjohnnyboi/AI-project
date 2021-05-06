from queue import PriorityQueue

def astar(graph, h, start, goal):
    count = 0
    frontier = PriorityQueue()
    frontier.put((0, [start]))
    cost_so_far = {}
    cost_so_far[start] = 0
    while frontier:
        count += 1
        cost, node = frontier.get()
        current = graph.vertices[node[len(node) - 1]]
        if current.visited == False:
            current.visited = True
            if current.name == goal:
                return node, cost;
            for vertexName, edgeCost in current.neighbors.items():
                if graph.vertices[vertexName].visited == False:
                    temp = node[:]
                    temp.append(vertexName)
                    new_cost = cost_so_far[current.name] + edgeCost
                    heuristicValue = h[vertexName]
                    frontier.put((new_cost + heuristicValue, temp))
                    cost_so_far[vertexName] = new_cost

from queue import PriorityQueue

def uniform_cost_search(graph, h, start, goal):
    count = 0
    frontier = PriorityQueue()
    frontier.put((0, [start]))
    while frontier:
        count += 1
        cost, node = frontier.get()
        current = graph.vertices[node[len(node) - 1]]
        if current.visited == False:
            current.visited = True
            if current.name == goal:
                return node, cost, count;
                break
            for vertexName, edgeCost in current.neighbors.items():
                if graph.vertices[vertexName].visited == False:
                    temp = node[:]
                    temp.append(vertexName)
                    new_cost = cost + edgeCost
                    frontier.put((new_cost, temp))

def DFSUtil(graph, v, visited, end):
    # Mark the current node as visited
    # and print it
    visited[v] = True
    print(v, end=' ')
    if (v == end):
        return;
    # Recur for all the vertices
    # adjacent to this vertex
    for i in graph.graph[v]:
        if visited[i] == False:
            if i == end:
                print(v, end=' ')
                return
            graph.DFSUtil(i, visited)

        # The function to do DFS traversal. It uses


# recursive DFSUtil()
def DFS(graph, v, end):
    # Mark all the vertices as not visited
    visited = graph
    # Call the recursive helper function
    # to print DFS traversal
    DFSUtil(graph, v, visited, end)

import graph
import bfs
import dfs

g = graph.Graph()

vertices = ['Arad', 'Zerind', 'Timisoara', 'Sibiu', 'Oradea', 'Lugoj', 'RimnicuVilcea',
            'Mehadia', 'Craiova', 'Pitesti', 'Fagaras', 'Dobreta', 'Bucharest', 'Giurgiu']

for i in vertices:
    g.add_vertex(graph.Vertex(i))

# g.print_graph()
edges = {
    'Arad': {'Zerind': 75, 'Sibiu': 140},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Oradea': 151, 'Fagaras': 99, 'RimnicuVilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Craiova': {'Dobreta': 120, 'RimnicuVilcea': 146, 'Pitesti': 138},
    'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138},
    'Fagaras': {'Bucharest': 211},
    'Dobreta': {'Craiova': 120},
    'Bucharest': {'Pitesti': 101, 'Giurgiu': 90}
}

for vertex1, value in edges.items():
    for vertex2, cost in edges[vertex1].items():
        g.add_edge(vertex1, vertex2, cost)

route, cost = bfs.breadthSearch(g, g.vertices["Arad"], 'Bucharest')
dfs.DFS(g, g.vertices["Arad"], 'Bucharest')
text = ""
for i in route:
    if text == "":
        text += i;
    else:
        text += ", "+i;
print(text);
print ("The cost is: "+str(cost))

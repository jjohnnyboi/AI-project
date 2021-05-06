import graph
import bfs
import ucs
import copy
'''from tkinter import *

window = Tk()
window.geometry("400x300")

window.title("Search algorithms app")

window.mainloop()'''
def getGraph():
    g = graph.Graph()

    vertices = ['Arad', 'Zerind', 'Timisoara', 'Sibiu', 'Oradea', 'Lugoj', 'RimnicuVilcea',
                'Mehadia', 'Craiova', 'Pitesti', 'Fagaras', 'Dobreta', 'Bucharest', 'Giurgiu']

    for i in vertices:
        g.add_vertex(graph.Vertex(i))
    edges = { 'Arad': {'Zerind': 75, 'Sibiu': 140},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Sibiu': {'Oradea': 151, 'Fagaras': 99, 'RimnicuVilcea': 80},
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
        'Craiova': {'Dobreta': 120, 'RimnicuVilcea': 146, 'Pitesti': 138},
        'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138},
        'Fagaras': {'Bucharest': 211},
        'Dobreta': {'Craiova': 120},
        'Bucharest': {'Pitesti': 101, 'Giurgiu': 90}}
    for vertex1, value in edges.items():
        for vertex2, cost in edges[vertex1].items():
            g.add_edge(vertex1, vertex2, cost)
    return g
heuristicValue =  {'Arad': 366, 'Zerind': 374,
         'Timisoara':200,
         'Sibiu': 253,
         'Oradea': 380,
         'Lugoj': 244, 'RimnicuVilcea': 193,
         'Mehadia': 241, 'Craiova': 160,
         'Pitesti': 10, 'Fagaras': 176,
         'Dobreta': 242, 'Bucharest': 0,
         'Giurgiu': 77}




while True:
    print("----------------------------------------------")
    print("----------------------------------------------")
    print("Choose an algorithim")
    print("1- BFS")
    print("2- UCS")
    print("3- A*")
    print("----------------------------------------------")
    print("----------------------------------------------")
    algoChoice = input("");
    currentGraph = getGraph();
    if (int(algoChoice) == 1):
        route, cost = bfs.breadthSearch(currentGraph, currentGraph.vertices["Arad"], 'Bucharest')
    elif (int(algoChoice) == 2):
        route, cost = ucs.uniform_cost_search(currentGraph, heuristicValue, 'Arad', "Bucharest")
    elif (int(algoChoice) == 3):
        route, cost = ucs.uniform_cost_search(currentGraph, heuristicValue, 'Arad', "Bucharest")

    text = ""
    for i in route:
        if text == "":
            text += i;
        else:
            text += ", "+i;
    print(text);
    print ("The cost is: "+str(cost))
    val = input("Do you want to use another algoirthm(Y/N)")
    if (val == "y"):
        currentGraph.setitFalse();


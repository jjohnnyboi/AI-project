import graph
import bfs
import ucs
import dfs
import gbfps
import astar

import tkinter as tk
from tkinter import ttk


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


window = tk.Tk()
window.title("Search algorithms")
wX = window.winfo_screenwidth()
wY = window.winfo_screenheight()
x = (wX/2) - 175
y = (wY/2) - 125
window.geometry('350x250+'+str(x.__round__())+"+"+str(y.__round__()))



# from select
ttk.Label(window, text="From:",font=("Times New Roman", 10)).grid(column=1,row=14, padx=15,pady=10)
n = tk.StringVar()
fromcity = ttk.Combobox(window, width=15,state="readonly")
fromcity['values'] = ('Arad', 'Zerind', 'Timisoara', 'Sibiu', 'Oradea', 'Lugoj', 'RimnicuVilcea','Mehadia', 'Craiova', 'Pitesti', 'Fagaras', 'Dobreta', 'Bucharest', 'Giurgiu')
fromcity.grid(column=1, row=15, padx=15,pady=10)
fromcity.current(0)
# to select
ttk.Label(window, text="to:",font=("Times New Roman", 10)).grid(column=2,row=14, padx=15,pady=10)
n = tk.StringVar()
tocity = ttk.Combobox(window, width=15,state="readonly")
tocity['values'] = ('Arad', 'Zerind', 'Timisoara', 'Sibiu', 'Oradea', 'Lugoj', 'RimnicuVilcea','Mehadia', 'Craiova', 'Pitesti', 'Fagaras', 'Dobreta', 'Bucharest', 'Giurgiu')
tocity.grid(column=2, row=15, padx=15,pady=10)
tocity.current(12)
# algo select
ttk.Label(window, text="Choose an algoirthm:",font=("Times New Roman", 10)).grid(column=1,row=20, padx=15,pady=10)
n = tk.StringVar()
algochoice = ttk.Combobox(window, width=15,state="readonly")
algochoice['values'] = ("BFS", "DFS", "UCS", "Greedy BFS", "A*")
algochoice.grid(column=1, row=21, padx=15,pady=10)
algochoice.current(0)


B = ttk.Button(window, text ="Run search", width=20)
B.grid(column=1, row=22)

ttk.Label(window, text="Route taken:",font=("Times New Roman", 10)).grid(column=2,row=20, padx=15,pady=10)
T = tk.Text(window, height = 4, width = 22,state="disabled")
T.configure(font=("Times New Roman", 12))
T.grid(column=2, row=21)
costLabel = tk.StringVar()
costLabel.set("The cost is: ")
ttk.Label(window, textvariable=costLabel,font=("Times New Roman", 10)).grid(column=2,row=22, padx=15,pady=10)

def compute():
    currentGraph = getGraph();
    if (fromcity.get() == tocity.get()):
        T.config(state="normal")
        T.delete(1.0, "end")
        T.insert(1.0, "You are already in "+fromcity.get())
        T.config(state="disabled")
        return;
    count = 0;
    if algochoice.get() == "BFS":
        route, cost = bfs.breadthSearch(currentGraph, currentGraph.vertices[fromcity.get()], tocity.get())
    elif algochoice.get() == "DFS":
        route, cost = dfs.depthSearch(currentGraph, currentGraph.vertices[fromcity.get()], tocity.get())
    elif algochoice.get() == "UCS":
        route, cost, count = ucs.uniform_cost_search(currentGraph, heuristicValue, fromcity.get(), tocity.get())
    elif algochoice.get() == "Greedy BFS":
        route, cost = gbfps.greedybfs(currentGraph, currentGraph.vertices[fromcity.get()], tocity.get())
    elif algochoice.get() == "A*":
        route, cost, count = astar.astar(currentGraph, heuristicValue, fromcity.get(), tocity.get())
    text = ""
    for i in route:
        if text == "":
            text += i;
        else:
            text += ", "+i;
    currentGraph.setitFalse();
    T.config(state="normal")
    T.delete(1.0, "end")
    T.insert(1.0,text)
    costLabel.set("The cost is: "+str(cost))
    if count != 0:
        costLabel.set("The cost is: " + str(cost)+ "\nCount: "+str(count))

    T.config(state="disabled")

B["command"] = compute;
window.mainloop()

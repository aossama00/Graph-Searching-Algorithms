
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
from array import *
LARGEFONT = ("Verdana", 35)

searchnumber = 0
z = 0
array
My_Dict = {}
DFSList = {}
BFSlist = {}
greadyList = {}
startNode = 'a'
EndNode = 'b'
numberOdNodes = 0
numberOfEdges = 0

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp




    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Enter Start Node", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=2, padx=10, pady=10)

        entry1 = tk.Entry(self,width = 75)
        entry1.grid(row=1, column=2, padx=10, pady=10)

        label2 = ttk.Label(self, text="Enter number of nodes", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label2.grid(row=2, column=2, padx=10, pady=10)

        entry2 = tk.Entry(self, width=75)
        entry2.grid(row=3, column=2, padx=10, pady=10)

        label3 = ttk.Label(self, text="Enter number edges", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label3.grid(row=4, column=2, padx=10, pady=10)

        entry3 = tk.Entry(self, width=75)
        entry3.grid(row=5, column=2, padx=10, pady=10)

        label4 = ttk.Label(self, text="Enter goal node", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label4.grid(row=6, column=2, padx=10, pady=10)

        entry4 = tk.Entry(self, width=75)
        entry4.grid(row=7, column=2, padx=10, pady=10)


        def takevalues():
            x = int(entry3.get())
            y = int(entry2.get())

            #start
            l = entry1.get()
            #goal
            u = entry4.get()
            global startNode
            global EndNode

            startNode = l
            EndNode = u

            global numberOdNodes
            global numberOfEdges
            numberOdNodes = y
            numberOfEdges = x
            global  array


            rows, cols = (x, y)
            array = [[0] * cols for _ in range(rows)]



            print(array)

        button1 = ttk.Button(self, text="Enter Nodes",
                             command=lambda: [controller.show_frame(Page1),takevalues()])

        # putting the button in its place by
        # using grid
        button1.grid(row=6, column=1, padx=10, pady=10)




# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Enter The Node", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=2, padx=10, pady=10)

        entry1 = tk.Entry(self, width=75)
        entry1.grid(row=1, column=2, padx=10, pady=10)

        label2 = ttk.Label(self, text="Enter The neighbours", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label2.grid(row=2, column=2, padx=10, pady=10)

        entry2 = tk.Entry(self, width=75)
        entry2.grid(row=3, column=2, padx=10, pady=10)

        def takevalues():
            x =entry1.get()
            y =entry2.get()

            global array
            global z

            print(array)

            array[z][0] = x
            print(z)

            strlen = len(str(y))
            print(strlen)

            for i in range(1,strlen+1):
                array[z][i] = y[i-1]


            # for i in range (1,((y).join(y)).count(y)):
            #
            #     array[z][i] = y[i]

            z = z + 1

            print (array)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Done",
                             command=lambda: [controller.show_frame(Page2),takevalues()])

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)



# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Node added successfully", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)


        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Enter the next node",
                             command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)


#----------------------------

        def Start_Graphing():

            G = nx.DiGraph()
            nodesList = []
            # nodesList2 = ['A','B']
            # nn = input("Please enter the number of nodes: ")

            global My_Dict
            global array
            global DFSList
            global BFSlist
            for n in range(0, numberOdNodes):
                # node = input("please enter the node: ")
                # nodesList.append(node)
                My_Dict[f'{array[n][0]}'] =[]
                # numberOfEdges = input("Please enter the number of edges: ")
                for j in range(1, int(numberOfEdges)):

                   if(array[n][j] != 0):
                    G.add_edges_from([(f'{array[n][0]}', f'{array[n][j]}')])

                    My_Dict[array[n][0]].append(array[n][j])
            global searchnumber
            if(searchnumber == 1):
                val_map = BFSlist
            elif(searchnumber == 2):
                val_map = DFSList
            elif (searchnumber == 3):
                val_map = UCSList
            elif (searchnumber == 4):
                val_map = greadyList
            elif(searchnumber == 5):
                val_map = AstarList
            else:
                val_map = {}
            # val_map[f'{nodesList2}']

            values = [val_map.get(node, 0.25) for node in G.nodes()]

            pos = nx.spring_layout(G)
            nx.draw_networkx_nodes(G, pos, node_size=200, cmap=plt.get_cmap('jet'), node_color=values)

            nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
            nx.draw_networkx_labels(G, pos)
            #


            plt.show()


        #------------------------------
        #DFS function----------------------------------------------------------------

        visited = set()  # Set to keep track of visited nodes.

        def dfs(visited, graph ,node, end):
            global My_Dict
            global DFSList
            global searchnumber
            searchnumber = 2
            global startNode
            global EndNode
            if end in visited:
                return
            if (node not in visited):
                print(node)
                DFSList[f'{node}'] = 1.0
                print(DFSList)
                visited.add(node)
                for nodes in graph[node]:
                    dfs(visited,graph,nodes, end)
        #-------------------------------BFS--------------------------------------

        visited2 = []  # List to keep track of visited nodes.


        def bfs(visited, graph, node, stop):
            global searchnumber
            global BFSlist
            searchnumber = 1
            queue = []  # Initialize a queue
            visited.append(node)
            queue.append(node)

            while queue:
                s = queue.pop(0)
                # Result[f'{s}'] = f'{s}'
                print(s, end=" ")
                BFSlist[f'{s}'] = 1.0
                if s == stop: return

                for neighbour in graph[s]:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.append(neighbour)

        #--------------------------------------------------------------
        from collections import deque
        # class Graph2:
        #     adjacency_list = My_Dict
        #     global greadyList
        #     global searchnumber
        #     searchnumber = 4
        #     # example of adjacency list (or rather map)
        #     # adjacency_list = {
        #     # 'A': [('B', 1), ('C', 3), ('D', 7)],
        #     # 'B': [('D', 5)],
        #     # 'C': [('D', 12)]
        #     # }
        #     def __init__(self, adjacency_list):
        #         self.adjacency_list = adjacency_list
        #
        #     def get_neighbors(self, v):
        #         return self.adjacency_list[v]
        #
        #     # heuristic function with equal values for all nodes
        #     def h(self, n):
        #         H = {
        #             'Q': 1,
        #             'W': 1,
        #             'E': 1,
        #             'R': 1,
        #             'T': 1,
        #             'Y': 1,
        #             'U': 1,
        #             'I': 1,
        #             'O': 1,
        #             'P': 1,
        #             'A': 1,
        #             'S': 1,
        #             'D': 1,
        #             'F': 1,
        #             'G': 1,
        #             'H': 1,
        #             'J': 1,
        #             'K': 1,
        #             'L': 1,
        #             'Z': 1,
        #             'X': 1,
        #             'C': 1,
        #             'V': 1,
        #             'B': 1,
        #             'N': 1,
        #             'M': 1
        #         }
        #         return H[n]
        #
        #         def Greedy_algorithm(self, start_node, stop_node):
        #
        #             # open_list is a list of nodes which have been visited, but who's neighbors
        #             # haven't all been inspected, starts off with the start node
        #             # closed_list is a list of nodes which have been visited
        #             # and who's neighbors have been inspected
        #             open_list = set([start_node])
        #             closed_list = set([])
        #             # g contains current distances from start_node to all other nodes
        #             # the default value (if it's not found in the map) is +infinity
        #             g = {}
        #             g[start_node] = 0
        #             # parents contains an adjacency map of all nodes
        #             parents = {}
        #             parents[start_node] = start_node
        #             while len(open_list) > 0:
        #                 n = None
        #                 # find a node with the lowest value of f() - evaluation function
        #                 for v in open_list:
        #                     if n == None or 0 + self.h(v) < 0 + self.h(n):
        #                         n = v;
        #                 if n == None:
        #                     print('Path does not exist!')
        #                     return None
        #                 # if the current node is the stop_node
        #                 # then we begin reconstructin the path from it to the start_node
        #                 if n == stop_node:
        #                     reconst_path = []
        #                     while parents[n] != n:
        #                         reconst_path.append(n)
        #                         n = parents[n]
        #                     reconst_path.append(start_node)
        #                     reconst_path.reverse()
        #                     print('Path found: {}'.format(reconst_path))
        #                     greadyList = reconst_path
        #                     return reconst_path
        #                 # for all neighbors of the current node do
        #                 for (m) in self.get_neighbors(n):
        #                     # if the current node isn't in both open_list and closed_list
        #                     # add it to open_list and note n as it's parent
        #                     if m not in open_list and m not in closed_list:
        #                         open_list.add(m)
        #                         parents[m] = n
        #                         g[m] = 0
        #                     # otherwise, check if it's quicker to first visit n, then m
        #                     # and if it is, update parent data and g data
        #                     # and if the node was in the closed_list, move it to open_list
        #                     else:
        #                         if g[m] > 0:
        #                             g[m] = 0
        #                             parents[m] = n
        #                             if m in closed_list:
        #                                 closed_list.remove(m)
        #                                 open_list.add(m)
        #                 # remove n from the open_list, and add it to closed_list
        #                 # because all of his neighbors were inspected
        #                 open_list.remove(n)
        #                 closed_list.add(n)
        #             print('Path does not exist!')
        #             return None
        #
            #--------------------------------------------------------------

        button2 = ttk.Button(self, text="SHOW GRAPH", command=lambda:Start_Graphing())

        # putting the button in its place by
        # using grid
        button2.grid(row=5, column=1, padx=10, pady=10)
        button3 = ttk.Button(self, text="BFS",
                             command=lambda: bfs(visited2,My_Dict,startNode,EndNode))
        button3.grid(row=6, column=1, padx=10, pady=10)

        button4 = ttk.Button(self, text="DFS",
                             command=lambda: dfs(visited,My_Dict,startNode,EndNode))
        button4.grid(row=7, column=1, padx=10, pady=10)

        button5 = ttk.Button(self, text="UCS",
                             command=lambda: controller.show_frame(Page1))
        button5.grid(row=8, column=1, padx=10, pady=10)

        button6 = ttk.Button(self, text="A star",
                             command=lambda: controller.show_frame(Page1))
        button6.grid(row=9, column=1, padx=10, pady=10)

        button7 = ttk.Button(self, text="Gready",command=lambda: Greedy_algorithm(startNode,EndNode))
        button7.grid(row=10, column=1, padx=10, pady=10)




# graph function




# Driver Code
app = tkinterApp()
app.mainloop()
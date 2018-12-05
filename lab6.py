from topological_sort import topological_sort
from kruskal_algorithm import kruskal_algorithm
from GraphAM import GraphAM

def display_menu(graph):        #   Method for displaying the mennu
    global count
    menu = {}
    menu['1'] = "MST KRUSKAL"
    menu['2'] = "TOPOLOGICAL SORT"
    menu['3'] = "Exit"
    while True:
        options = menu.keys()

        for entry in options:
            print(entry, ".- ", menu[entry])
        selection = input("Please Select:")
        if selection == '1':
            while True:
                print("S = Source, D = Destination, W = Weight")
                print("   MST  ")
                print(" S  D  W ")
                minimumSpanningTree = kruskal_algorithm(graph)
                for i in range(len(minimumSpanningTree)):
                    print(minimumSpanningTree[i])
                selection = input("Press 0 to go back to the menu: ")
                if selection == '0':
                    break
                else:
                    print("Unknown Option Selected!")
        elif selection == '2':
            while True:
                print('Topological Sort')
                print(topological_sort(graph))
                selection = input("Press 0 to go back to the menu: ")
                if selection == '0':
                    break
                else:
                    print("Unknown Option Selected!")
        elif selection == '3':
            print("Bye")
            break
        else:
            print("Unknown Option Selected!")


if __name__ == '__main__':
    graph = GraphAM(6,True)     #Creating the graph
    graph.add_edge(0, 1, 1)     #Vertex 0, dest 1, weight 1
    graph.add_edge(0, 3, 2)
    graph.add_edge(0, 4, 5)
    graph.add_edge(1, 2, 7)
    graph.add_edge(1, 4, 3)
    graph.add_edge(3, 4, 1)
    graph.add_edge(4, 2, 5)
    graph.add_edge(4, 5, 1)
    graph.add_edge(5, 2, 1)

    display_menu(graph) #Display menu



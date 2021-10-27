import csv
import networkx as nx
import matplotlib.pyplot as plt
def readNetwork():
    G = nx.DiGraph()
    my_file = open('fileEdges', encoding="utf-8")
    data = csv.reader(my_file)
    for edge in data:
        if len(edge)>0 :
            G.add_edge(edge[0].lower()[0:75], edge[1].lower()[0:75])
    print('network created')
    return G

def analyzeNetwork(G):
    print('number of Nodes:',G.number_of_nodes())
    print('number of Links:',G.number_of_edges())
    print('clustering coeficients:', nx.clustering(G))
    print('average distance:', nx.average_shortest_path_length(G))
    plt.plot(nx.degree_histogram(G), 'ro', label = 'Degree Dist')
    plt.show()
analyzeNetwork(readNetwork())


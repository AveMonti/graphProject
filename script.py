import networkx as nx
import matplotlib.pyplot as plt

from getRoouts import getRoots

if __name__ == "__main__":
    myGraph = {0: [1,2,3], 1: [], 2: [1], 3: [4,5],4: [3,5], 5: [3,4,7], 6: [8], 7: [],8: [9], 9: []}
    xyz = getRoots(myGraph)
    list = []
    for keys in xyz.keys():
        for x in (xyz[keys]):
            value = (keys, x)
            list.append(value)

        # print (xyz[keys][1])

    print(getRoots(myGraph))
    print(list)

    G = nx.DiGraph()
    G.add_edges_from(list)
    val_map = {'A': 1.0,
               'D': 0.5714285714285714,
               'H': 0.0}

    values = [val_map.get(node, 0.25) for node in G.nodes()]
    red_edges = [('A', 'C'), ('E', 'C')]
    edge_colours = ['black' if not edge in red_edges else 'red'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_color = values, node_size = 500)
    nx.draw_networkx_labels(G, pos)
    # nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    plt.show()

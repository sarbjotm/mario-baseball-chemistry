import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import xlrd


def create_graph():
    G = nx.Graph()
    nodes = ["Mario", "Luigi", "Donkey Kong", "Diddy Kong", "Peach", "Daisy", "Yoshi", "Baby Mario", "Baby Luigi",
             "Bowser", "Wario", "Waluigi", "Koopa", "Toad", "Boo", "Toadette", "Shyguy", "Birdo", "Monty Mole",
             "Bowser Jr", "Paratroopa", "Pianta", "Noki", "Hammer Bro", "Toadsworth", "Kamek", "King Boo",
             "Dixie Kong", "Petey Piranha", "Goomba", "Paragoomba", "Dry Bones"]
    FILE_PATH = "database.xls"
    x1 = pd.ExcelFile(FILE_PATH)
    df = x1.parse("Sheet1")
    G.add_nodes_from(nodes)
    for i in range(0, len(nodes)):
        for j in range(0, len(nodes)):
            #If not connected then add_edge
            G.add_edge(nodes[i], nodes[j], weight=df[nodes[j]].values[i])
    return G


def main():
    graph = create_graph()
    nx.draw(graph,
            with_labels=True,
            node_color='black',
            node_size=18,
            font_size=8,
            verticalalignment='baseline',
            edge_color='grey')
    plt.show()
    print(f"WEIGHT from Mario to Bowser is: {graph['Mario']['Bowser']['weight']}")


if __name__ == '__main__':
    main()

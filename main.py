import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    G = nx.Graph()
    nodes = ["Mario", "Luigi", "Donkey Kong", "Diddy Kong", "Peach", "Daisy", "Yoshi", "Baby Mario", "Baby Luigi",
             "Bowser", "Wario", "Waluigi", "Koopa", "Toad", "Boo", "Toadette", "Shyguy", "Birdo", "Monty Mole",
             "Bowser Jr", "Paratroopa", "Pianta", "Noki", "Hammer Bros", "Toadsworth", "Kamek", "King Boo",
             "Dixie Kong", "Petey Piranha", "Goomba", "Paragoomba", "Dry Bones"]
    G.add_nodes_from(nodes)
    for i in range(0, len(nodes)):
        for j in range(0, len(nodes)):
            if nodes[i] != nodes[j]:
                G.add_edge(nodes[i], nodes[j])
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


if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import networkx as nx

from networkx.drawing.nx_agraph import graphviz_layout


def main():
    tree = nx.DiGraph()

    nodes = [
        ('project', {}),
        ('restrict', {}),
        ('join', {}),
        ('Table Customer', {}),
        ('Table Order', {})
    ]

    edges = [
        ('project', 'restrict'),
        ('restrict', 'join'),
        ('join', 'Table Customer'),
        ('join', 'Table Order')
    ]

    tree.add_nodes_from(nodes)
    tree.add_edges_from(edges)

    fig, ax = plt.subplots()
    pos = graphviz_layout(tree, prog='dot')
    nx.draw(tree, pos=pos, with_labels=True, ax=ax)
    plt.show()


if __name__ == '__main__':
    main()

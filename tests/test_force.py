from py3js.network import ForceDirectedGraph, Node, Link
from random import randint


def test_generates_html():
    g = ForceDirectedGraph(1000, 500)
    g.add_node(Node("source", "test tooltip"))
    g.add_node(Node("dest #1", color="green"))
    g.add_link(Link("source", "dest #1"))
    s = g._repr_html_()
    g.save("c:\\tmp\\1.html")
    print(s)


def test_multi_level():
    g = ForceDirectedGraph(1000, 1000, x_levels=5, collision_radius=1, show_node_names=False)

    for i in range(0, 10):
        g.add_node(Node(f"lvl1 #{i}", tooltip=f"lvl1 #{i}", level=1, radius=randint(1, 40)))

    for i in range(0, 100):
        g.add_node(Node(f"lvl2 #{i}", level=2, color="green", radius=randint(1, 15)))

    for i in range(0, 100):
        g.add_node(Node(f"lvl3 #{i}", level=3, color="blue", radius=randint(1, 5)))

    g.save("c:\\tmp\\1.html")

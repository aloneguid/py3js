from py3js.network import ForceDirectedGraph, Node, Link
from random import randint

save_path = "c:\\tmp\\1.html"


def test_simplest():
    g = ForceDirectedGraph(1000, 500)

    nodes = ["dev", "pre-prod", "prod", "developers", "testers", "managers"]
    colours = ["green", "green", "green", "blue", "blue", "blue"]

    for n, c in zip(nodes, colours):
        g.add_nodes(Node(n, color=c))

    # link process
    g.add_links(Link("dev", "pre-prod"))
    g.add_links(Link("pre-prod", "prod"))

    # link involved
    g.add_links(Link("developers", "dev"))
    g.add_links(Link("developers", "pre-prod"))
    g.add_links(Link("testers", "pre-prod"))
    g.add_links(Link("managers", "prod"))

    g.save(save_path)


def test_labels_and_strokes():
    g = ForceDirectedGraph(show_node_names=True)
    g.add_nodes(Node("one", radius=10))
    g.add_nodes(Node("two", radius=20))
    g.add_nodes(Node("three", radius=20))
    g.add_nodes(Node("red border", stroke_color="red", stroke_width=5))
    g.save(save_path)


def test_multi_level():
    g = ForceDirectedGraph(1000, 1000, x_levels=5, collision_radius=1, show_node_names=False)

    for i in range(0, 10):
        g.add_nodes(Node(f"lvl1 #{i}", tooltip=f"lvl1 #{i}", level=1, radius=randint(1, 40)))

    for i in range(0, 100):
        g.add_nodes(Node(f"lvl2 #{i}", level=2, color="green", radius=randint(1, 15)))

    for i in range(0, 100):
        g.add_nodes(Node(f"lvl3 #{i}", level=3, color="blue", radius=randint(1, 5)))

    g.save("c:\\tmp\\1.html")

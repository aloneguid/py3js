from py3js.network import ForceDirectedGraph, Node, Link
from random import randint

save_path = "c:\\tmp\\1.html"


def test_simplest():
    g = ForceDirectedGraph(800, 200)

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
    print(g._repr_html_())


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

    # link some
    for i in range(0, 2):
        n_from = f"lvl1 #{randint(0, 10)}"
        n_to = f"lvl2 #{randint(0, 100)}"
        g.add_links(Link(n_from, n_to, opacity=0.1, is_arrow=False))


    g.save("c:\\tmp\\1.html")


def test_twitter_nel():
    path = "c:\\tmp\\TWITTER-Real-Graph-Partial.nel"
    with open(path, "r") as reader:
        lines = reader.readlines()

    g = ForceDirectedGraph(1000, 1000, collision_radius=20, show_node_names=True)

    # n 1 apple
    # n 2 store
    # n 3 buy
    # n 4 mac
    # e 1 2 3.034013E-4
    # e 3 4 1.6500772E-4
    # e 3 2 3.5130675E-4
    # g 2191352508 56

    mp = dict()
    for line in lines[:10]:
        pts = line.split(" ")
        if len(pts) >= 3:
            if pts[0] == "n":
                id = pts[1]
                name = pts[2]
                g.add_nodes(Node(id, name, f"id: {id}, name: {name}", radius=3, stroke_width=0))
                mp[id] = name
            if pts[0] == "e":
                id_from = pts[1]
                id_to = pts[2]
                g.add_links(Link(id_from, id_to))
        else:
            mp = dict()


    g.save(save_path)

    print(len(lines))



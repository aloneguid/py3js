from py3js.network import ForceDirectedGraph, Node, Link


def test_generates_html():
    g = ForceDirectedGraph(1000, 500)
    g.add_node(Node("source", "test tooltip"))
    g.add_node(Node("dest #1", color="green"))
    g.add_link(Link("source", "dest #1"))
    s = g._repr_html_()
    g.save("c:\\tmp\\1.html")
    print(s)

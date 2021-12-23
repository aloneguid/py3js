from py3js.tree import Tree, Node, TreeKind

save_path = "c:\\tmp\\1.html"

def test_simplest():

    root = Node("programming", [
        Node("C++"),
        Node("Python"),
        Node("C#"),
        Node("Scala")
    ])

    t = Tree(root, TreeKind.RADIAL_TIDY)
    t.save(save_path)
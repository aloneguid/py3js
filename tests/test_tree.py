from py3js.tree import Tree, Node

save_path = "c:\\tmp\\1.html"

def test_simplest():

    root = Node("programming", [
        Node("C++"),
        Node("Python"),
        Node("C#"),
        Node("Scala")
    ])

    t = Tree(root)
    t.save(save_path)
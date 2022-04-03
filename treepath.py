from collections import namedtuple

def count(node):
    # TODO

if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(Node(None,None),Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 8
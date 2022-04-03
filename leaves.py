from ast import Div
from collections import namedtuple

def count(node):
    if not node: 
        return 0
    elif not node.left and not node.right: 
        return 1
    return count(node.left) + count(node.right)
    

if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 2
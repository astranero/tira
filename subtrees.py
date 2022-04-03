from collections import namedtuple

def diff(node):
    if not node: return 0

    difference = abs(nodes_count(node.left) - nodes_count(node.right))
    return max(max(difference,diff(node.left)), max(difference,diff(node.right)))

def nodes_count(node):
    if not node: return 0
    return 1 + nodes_count(node.left)+nodes_count(node.right)

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=None))
    print(diff(tree)) # 3
from turtle import *
from collections import namedtuple

Node = namedtuple("Node",["left","right"])

def count(node):
    if not node:
        return 0
    return count(node.left)+count(node.right)+1

def draw_tree(node,x,y):
    if not node:
        return
    goto(x,y)
    stamp()
    if node.left:
        draw_tree(node.left,x-(count(node.left.right)+1)*30,y-40)
        goto(x,y)
    if node.right:
        draw_tree(node.right,x+(count(node.right.left)+1)*30,y-40)
        goto(x,y)

# tässä on binääripuu, joka halutaan piirtää
tree = Node(
    Node(Node(None,None),Node(None,None)),
    Node(Node(None,None),Node(None,None))
)

shape("circle")
draw_tree(tree,0,0)
done()
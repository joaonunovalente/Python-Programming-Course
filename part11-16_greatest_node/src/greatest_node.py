# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def compare_nodes(node1: Node, node2: Node):
    if node1.value > node2.value:       
        return node1
    return node2

def helper_function(root: Node):
    node_maximum = root

    if root.left_child is not None:
        node_maximum = compare_nodes(node_maximum, helper_function(root.left_child))

    if root.right_child is not None:
        node_maximum = compare_nodes(node_maximum, helper_function(root.right_child))
    
    return node_maximum

def greatest_node(root: Node):
    node_maximum = helper_function(root)

    return node_maximum.value

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    
    
    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)
    tree.right_child.left_child = Node(13)

    print(greatest_node(tree))
# 10.17.2015
# http://www.geeksforgeeks.org/construct-a-binary-tree-from-parent-array-representation/

class Tree():
    def __init__(self, root):
        self.root = root
    def __str__(self):
        return "Root: " + str(self.root)

class Node():
    def __init__(self, value, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
    def __str__(self):
        return str(self.value) + " | " + str(self.left_child) + " | " + str(self.right_child)

def main():
    parent = [1,5,5,2,2,-1,3]
    index = [i for i,j in enumerate(parent) if j == -1]
    root = Node(index[0])
    buildTree(parent, root)
    t = Tree(root)
    print t

def buildTree(array, node):
    index = [i for i,j in enumerate(array) if j == node.value]
    if len(index) == 0:
        return
    for i in index:
        if node.left_child == None:
            node.left_child = Node(i)
            buildTree(array, node.left_child)
        else:
            node.right_child = Node(i)
            buildTree(array, node.right_child)

if __name__ == '__main__':
    main()

# import ipdb; ipdb.set_trace()

a_depth = None
a_parent = None
b_depth = None
b_parent = None

class node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def cousins(root, A, B, depth = 0, ret = False):
    global a_depth
    global a_parent
    global b_depth
    global b_parent
    if root == None:
        return ret
    if root.value == A:
        a_depth = depth
        return ret
    if root.value == B:
        b_depth = depth
        return ret
    ret = cousins(root.left, A, B, depth + 1)
    ret = cousins(root.right, A, B, depth + 1)
    if a_depth != None and a_parent == None:
        a_parent = root
    if b_depth != None and b_parent == None:
        b_parent = root
    if a_parent != None and b_parent != None:
        if a_parent != b_parent and a_depth == b_depth:
            return True
        else:
            return False

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

# cousins(root,2,3)
print cousins(root,4,6)
